from django import forms
from .models import feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['title', 'text']
        labels = {'title': '标题', 'text': '内容'}
        widgets = {'text': forms.Textarea(attrs={'col': 80})}