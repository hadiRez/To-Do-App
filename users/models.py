from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
