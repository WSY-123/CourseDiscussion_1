from django.test import TestCase
from django.urls import reverse, resolve
from .models import User
from .views import login, register


class RegisterTest(TestCase):
    """用户注册页面测试"""

    def setUp(self):
        url = reverse('users:register')
        self.response = self.client.get(url)

    def test_register_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_register_url_resolves_view(self):
        view = resolve('/users/register/')
        self.assertEquals(view.func, register)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_form_inputs(self):
        '''
        此表单应该有7个输入： csrf, name, email, password1, password2，captcha(2),
        其中 crsf 和 captcha 的第一个 input是隐藏的,
        另外有2个选择框: sex, institute
        '''
        self.assertContains(self.response, '<input', 7)
        self.assertContains(self.response, '<select', 2)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class LoginTest(TestCase):
    """用户登录页面测试"""

    def setUp(self):
        User.objects.create(name='Bob', password='12345', email='12345@qq.com', sex='male', institute='电院')
        url = reverse('users:login')
        self.response = self.client.get(url)

    def test_login_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_login_url_resolves_view(self):
        view = resolve('/users/login/')
        self.assertEquals(view.func, login)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_form_inputs(self):
        """
        此表单应该有5个输入： csrf, name, password，captcha(2)，
        其中 crsf 和 captcha 的第一个 input是隐藏的
        """
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="password"', 1)
