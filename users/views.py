from django.shortcuts import render, redirect
from django.urls import reverse
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth import authenticate
from furl import furl
from django.http import HttpResponseRedirect
from .models import User
from .forms import UserForm, RegisterForm, PasswordResetForm
from . import models
import hashlib
import requests
import json


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
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
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
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.institute = institute
                new_user.save()
                return redirect('users:login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'users/register.html', locals())


def register_1(request, name, email):
    name = name
    email = email
    if request.session.get('is_login', None):
        # 登录状态不允许注册
        HttpResponseRedirect(reverse('home:homepage'))
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            # 获取数据
            username = name
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = email
            sex = register_form.cleaned_data['sex']
            institute = register_form.cleaned_data['institute']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return redirect(reverse('users:register_1', kwargs={'name': name, 'email': email}))
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return redirect(reverse('users:register_1', kwargs={'name': name, 'email': email}))
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return redirect(reverse('users:register_1', kwargs={'name': name, 'email': email}))

                # 当一切都OK的情况下，创建新用户
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.institute = institute
                new_user.save()
                user = models.User.objects.get(name=username)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return HttpResponseRedirect(reverse('home:homepage'))
    register_form = RegisterForm()
    return render(request, 'users/register_1.html', locals())


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
                if user.password == hash_code(password):
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
    f = furl(request.get_full_path())
    code = f.args['code']
    url = 'https://jaccount.sjtu.edu.cn/oauth2/token'
    client_id = 'sPu9ghxQjehvRUzH9SuY'
    client_secret = 'B0163EAEC431290BBA79D53246C861A76D9B51D692B08389'
    grant_type = 'authorization_code'
    redirect_uri = 'http://127.0.0.1:8000/users/process/'
    data = {
        'grant_type': grant_type,
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    result = requests.post(url, data)
    strResult = json.loads(result.text)
    id_token = strResult['id_token']
    access_token = strResult['access_token']
    headers = {"Authorization": "Bearer {}".format(access_token)}
    url = 'https://api.sjtu.edu.cn/v1/me/profile?access_token=' + access_token
    r = requests.request(url=url, method='GET', headers=headers, timeout=(20, 60))
    entities = json.loads(r.text).get('entities')
    print(entities)
    for item in entities:
        name = item['name']
        email = item['account']
    same_name_user = models.User.objects.filter(name=name)
    if same_name_user:  # 用户名唯一
        user = models.User.objects.get(name=name)
        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
        return HttpResponseRedirect(reverse('home:homepage'))
        #return HttpResponseRedirect('http://127.0.0.1:8000/users/login/')
    else:
        return redirect(reverse('users:register_1', kwargs={'name': name, 'email': email + '@sjtu.edu.cn'}))


def personalpage(request):
    if not request.session.get('is_login', None):
        # 如果本来未登录,则返回主页
        return HttpResponseRedirect(reverse('home:homepage'))
    user = User.objects.get(id=request.session.get('user_id'))
    context = {'user': user,
               'user_name': user.name,
               'user_email': user.email,
               'user_sex': user.sex,
               'user_institute': user.institute,
               }
    return render(request, 'users/personalpage.html', context)


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def password_reset(request):
    if not request.session.get('is_login', None):
        return HttpResponseRedirect(reverse('home:homepage'))

    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            old = form.cleaned_data['old_password']
            new1 = form.cleaned_data['new_password1']
            new2 = form.cleaned_data['new_password2']
            user = User.objects.get(id=request.session.get('user_id'))
            if user.password == hash_code(old):
                if new1 != new2:
                    message = "两次输入的密码不同！"
                    return render(request, 'users/password_reset.html', {'message': message})
                else:
                    user.password = hash_code(new1)
                    user.save()
                    request.session.flush()
                    return redirect(reverse('users:login'))  # 修改密码后重新登录
            else:
                message = "密码不正确！"
                form = PasswordResetForm()
                return render(request, 'users/password_reset.html', {'form': form, 'message': message})

    form = PasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})
