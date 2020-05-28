from django.test import TestCase
from django.urls import reverse, resolve
from users.models import User
from .views import index, question_details
from .forms import NewQuestionForm
from .models import Question, Answer, Tag, Comment


class IndexTest(TestCase):
    """问答主页测试"""

    def setUp(self):
        self.user = User.objects.create(name='Bob', password='12345', email='12345@qq.com', sex='male', institute='电院')
        self.question = Question.objects.create(title='title', body='test', asked_by=self.user)
        url = reverse('discuss:index')
        self.response = self.client.get(url)

    def test_index_views_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/discussion/')
        self.assertEquals(view.func, index)

    def test_index_views_contains_link_to_question_details(self):
        question_details_url = reverse('discuss:question_details', kwargs={'id': self.question.id})
        self.assertContains(self.response, 'href="{0}"'.format(question_details_url))


class QuestionDetailsTest(TestCase):
    """问题详情页测试"""

    def setUp(self):
        self.user = User.objects.create(name='Bob', password='12345', email='12345@qq.com', sex='male', institute='电院')
        Question.objects.create(title='title', body='test', asked_by=self.user)

    def test_question_details_view_success_status_code(self):
        url = reverse('discuss:question_details', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_details_url_resolves_view(self):
        view = resolve('/discussion/1/')
        self.assertEquals(view.func, question_details)


class NewQuestionTest(TestCase):
    """提问测试"""

    def setUp(self):
        self.user = User.objects.create(name='Bob', password='12345', email='12345@qq.com', sex='male', institute='电院')

    def test_ask_question_view_success_status_code(self):
        url = reverse('discuss:ask_question')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contains_form(self):
        url = reverse('discuss:ask_question')
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewQuestionForm)

    def test_ask_question_invalid_post_data(self):
        url = reverse('discuss:question_details',kwargs={'id':1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 404)
