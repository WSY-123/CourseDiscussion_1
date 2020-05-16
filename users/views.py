from django.shortcuts import render, redirect
from django.urls import reverse
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth import authenticate
from furl import furl
from django.http import HttpResponseRedirect
from .forms import UserForm
from . import models


# Create your views here.
def logout(request):
    """注销账户"""
    if not request.session.get('is_login', None):
        # 如果本来就未登录
        return HttpResponseRedirect(reverse('home:homepage'))
    request.session.flush()
    return HttpResponseRedirect(reverse('home:homepage'))


def register(request):
    """注册新用户"""
    if request.session.get('is_login', None):
        # 登录状态不允许注册
        HttpResponseRedirect(reverse('home:homepage'))
    if request.method == "POST":
        print('1')
        register_form = models.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            print('2')
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            institute = register_form.cleaned_data['institute']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'users/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'users/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'users/register.html', locals())
                # 当一切都OK的情况下，创建新用户
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.institute = institute
                new_user.save()
                return redirect('users:login')  # 自动跳转到登录页面
    register_form = models.RegisterForm()
    return render(request, 'users/register.html', locals())


def login(request):
    if request.session.get('is_login', None):
        return redirect('home:homepage')

    login_form = UserForm()
    if request.method != 'POST':
        print('1')
    else:
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return HttpResponseRedirect(reverse('home:homepage'))
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'users/login.html', locals())

    return render(request, 'users/login.html', locals())

def process(request):
    f=furl(request.get_full_path())
    CODE=f.args['code']
    print('成功获取CODE')
    return HttpResponseRedirect('https://api.sjtu.edu.cn/sns/oauth2/access_token?client_id=sPu9ghxQjehvRUzH9SuY&secret=B0163EAEC431290BBA79D53246C861A76D9B51D692B08389&code={{CODE}}&scope=openid')

def personalpage(request):
    if not request.session.get('is_login', None):
       # 如果本来未登录,则返回主页
         return HttpResponseRedirect(reverse('home:homepage'))
    context = {'user_name':request.user.username,
                'user_email':request.user.email,
                # 'user_sex':request.user.sex,
               }
    return render(request,'users/personalpage.html',context)
