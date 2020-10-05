from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff']

admin.site.register(User, UserAdmin)


