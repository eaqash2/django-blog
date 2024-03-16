from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


    def __str__(self) -> str:
        return self.email

'''    readonly_fields = [
        'created_at',
    ]'''



'''    def title(self, obj):
        return obj'''

admin.site.register(CustomUser, CustomUserAdmin)