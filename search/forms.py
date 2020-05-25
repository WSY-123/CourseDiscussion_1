from django import forms
from .models import feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['title', 'text']
        labels = {'title': '标题', 'text': '内容'}
        widgets = {'text': forms.Textarea(attrs={'col': 80})}

class SelectTestForm(forms.Form):
    SELVALUE = (
        ('标题', 'first'),
        ('内容', 'second'),
        ('作者', 'third'),
    )
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))
