from django.contrib import admin
from . import models

class lessons_admin(admin.ModelAdmin):
    list_display = ['name','teacher','institute','credit','semester',
                    'location','date_added']
    list_filter=['name','teacher','institute','credit','semester',
                 'location','date_added']
    search_fields = ['name','teacher','institute','credit','semester',
                    'location','date_added']

class feedback_admin(admin.ModelAdmin):
    list_display = ['title','date_added']
    list_filter = ['title','date_added']
    search_fields = ['date_added','title']

admin.site.register(models.lessons, lessons_admin)
admin.site.register(models.feedback, feedback_admin)

