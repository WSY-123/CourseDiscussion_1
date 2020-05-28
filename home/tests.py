from django.test import TestCase
from django.urls import reverse, resolve
from .views import homepage


class HomeTest(TestCase):
    """网站首页测试"""

    def setUp(self):
        url = reverse('home:homepage')
        self.response = self.client.get(url)

    def test_home_views_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_view(self):
        view = resolve('/')
        self.assertEquals(view.func, homepage)
