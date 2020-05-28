from django.forms import ModelForm
from django import forms
from .models import Tag, Question, Answer, Comment


class NewQuestionForm(ModelForm):
    """创建新问题表单"""
    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']
        labels = {'title': '标题', 'body': '问题描述', 'tags': '标签'}
        widgets = {
            'body': forms.Textarea(attrs={'rows': 8, 'placeholder': 'What a question it is?'}),
            'tags': forms.CheckboxSelectMultiple
        }


class NewAnswerForm(ModelForm):
    """回答问题表单"""
    class Meta:
        model = Answer
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Edit your answer here'})
        }


class AddCommentForm(ModelForm):
    """评论表单"""
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3})
        }


class AddTagForm(ModelForm):
    """添加新标签表单"""
    class Meta:
        model = Tag
        fields = ['name']
        labels = {'name': '标签名'}
        widgets = {
            'name': forms.Textarea(attrs={'rows': 1})
        }
