from django.shortcuts import render
from .forms import FeedbackForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    """搜索主页"""
    return render(request, 'search/index.html')

def feedback(request):
    """提交反馈"""
    if request.method != 'POST':
        #未提交数据
        form = FeedbackForm()
    else:
        #POST提交的数据，对数据进行处理
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'search/succeed.html')
    context = {'form': form}
    return render(request, 'search/feedback.html', context)
