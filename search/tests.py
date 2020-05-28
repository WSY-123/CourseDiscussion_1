from django.test import TestCase
from django.urls import reverse, resolve
from .views import index


class IndexTest(TestCase):
    """课程搜索主页测试"""

    def setUp(self):
        url = reverse('search:index')
        self.response = self.client.get(url)

    def test_index_views_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_view(self):
        view = resolve('/search/')
        self.assertEquals(view.func, index)

    def test_form_inputs(self):
        """
        此表单应该有2个输入： 关键字、提价按钮
        另外有2个选择框: 开课学院、开课学年。
        """
        self.assertContains(self.response, '<input', 2)
        self.assertContains(self.response, '<select', 2)
        self.assertContains(self.response, 'type="text"', 1)

