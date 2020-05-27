from django.contrib import admin

from . import models


class Question_admin(admin.ModelAdmin):
    list_display = ['title', 'create_at', 'views']
    list_filter = ['create_at']
    search_fields = ['title']


class Anwser_admin(admin.ModelAdmin):
    list_display = ['question', 'create_at']
    list_filter = ['create_at']
    search_fields = ['question']


class Comment_admin(admin.ModelAdmin):
    list_display = ['create_at']
    list_filter = ['create_at']
    search_fields = ['create_at']


# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Question, Question_admin)
admin.site.register(models.Answer, Anwser_admin)
admin.site.register(models.Comment, Comment_admin)
