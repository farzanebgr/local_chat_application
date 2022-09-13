from django.contrib import admin
from user_app import models

class UserModel(admin.ModelAdmin):
    list_display = ['username', 'email', 'last_login']
    list_filter = ['is_staff', 'is_active', 'user_status']

admin.site.register(models.User,UserModel)