# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

    #username = email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []