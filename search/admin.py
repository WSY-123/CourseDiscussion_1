from django.contrib import admin
<<<<<<< HEAD
from . import models

class lessons_admin(admin.ModelAdmin):
    list_display = ['name','teacher','institute','credit','semester',
                    'time','weeks','location','date_added']
    list_filter=['name','teacher','institute','credit','semester',
                 'time','weeks','location','date_added']
    search_fields = ['name','teacher','institute','credit','semester',
                     'time','weeks','location','date_added']

class feedback_admin(admin.ModelAdmin):
    list_display = ['title','date_added']
    list_filter = ['title','date_added']
    search_fields = ['date_added','title']

# Register your models here.
admin.site.register(models.lessons,lessons_admin)
admin.site.register(models.feedback,feedback_admin)
=======
from search.models import lessons, feedback

# Register your models here.
admin.site.register(lessons)
admin.site.register(feedback)
>>>>>>> 6ea765dc4c30afa813d6fca53147404be2d4ae49
