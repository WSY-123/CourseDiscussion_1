from django.contrib import admin
<<<<<<< HEAD
from .import models

class Question_admin(admin.ModelAdmin):
    list_display = ['title','create_at','votes','views']
    list_filter=['create_at']
    search_fields = ['title']

class Anwser_admin(admin.ModelAdmin):
    list_display = ['question','create_at']
    list_filter=['create_at']
    search_fields = ['question']

class Comment_admin(admin.ModelAdmin):
    list_display = ['create_at']
    list_filter=['create_at']
    search_fields = ['create_at']

# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Question,Question_admin)
admin.site.register(models.Answer,Anwser_admin)
admin.site.register(models.Comment,Comment_admin)
=======
from .models import Tag, Question, Answer, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Question)
>>>>>>> 6ea765dc4c30afa813d6fca53147404be2d4ae49
