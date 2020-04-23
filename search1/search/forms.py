from django import forms
from .models import feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        labels = {'title': '标题', 'text': '内容'}
        fields = ['title', 'text']
        widgets = {'text': forms.Textarea(attrs={'col':80})}