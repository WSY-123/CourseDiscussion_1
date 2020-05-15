from django.contrib import admin
from .import models

class User_admin(admin.ModelAdmin):
    list_display = ['name','email','sex','c_time']
    list_filter=['c_time']
    search_fields = ['name','sex','c_time']

# Register your models here.

admin.site.register(models.User,User_admin)
from users.models import User

