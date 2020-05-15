from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('process/', views.process, name='process'),
=======
>>>>>>> 6ea765dc4c30afa813d6fca53147404be2d4ae49
]
