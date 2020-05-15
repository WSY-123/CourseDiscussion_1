from django.forms import ModelForm
from django import forms
from .models import Tag, Question, Answer, Comment


class NewQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']
        labels = {'title':'标题', 'body': '问题描述', 'tags': '标签'}
        widgets = {
            'body': forms.Textarea(attrs={'rows': 8, 'placeholder': 'What a question it is?'}),
            'tags': forms.CheckboxSelectMultiple
        }


class NewAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Edit your answer here'})
        }


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3})
        }
