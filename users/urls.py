from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('process/', views.process, name='process'),
    path('personalpage/', views.personalpage, name='personalpage'),
]
