from django.contrib import admin
from django.urls import path
from . import views
from haystack.views import SearchView

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('course/', SearchView(), name='haystack_search'),
    path('feedback/', views.feedback, name='feedback'),
]