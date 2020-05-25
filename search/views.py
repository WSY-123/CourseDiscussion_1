from django.shortcuts import render
from .forms import FeedbackForm
from .models import lessons
from haystack.views import SearchView
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    """搜索主页"""
    institute = request.GET.get("institute")
    return render(request, 'search/index.html',institute)


def select(request):
    """筛选过后的结果"""
    institute = request.GET.get("institute")
    context={"institute":institute}
    SearchView(context)
    return render(request,'search/search.html')


def feedback(request):
    """提交反馈"""
    if request.method == 'POST':
        # POST提交的数据，对数据进行处理
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'search/succeed.html')
    else:
        # 未提交数据
        form = FeedbackForm()
        context = {'form': form}
        return render(request, 'search/feedback.html', context)


def show(request):
    """显示筛选页面"""
    list = lessons.objects.all()
    return render(request, 'search/show.html', )
