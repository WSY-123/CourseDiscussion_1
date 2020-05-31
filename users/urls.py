from django.urls import re_path, path, include
from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('register_1/?name=<name>&email=<email>/', views.register_1, name='register_1'),
    path('process/', views.process, name='process'),
    path('personalpage/', views.personalpage, name='personalpage'),
    path('passwordreset/', views.password_reset, name='password_reset')
]
