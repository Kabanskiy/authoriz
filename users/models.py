from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

class User(AbstractUser):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True) # уникальное поле, т.к. чз него будет вход
    password = models.CharField(max_length=250)

    USERNAME_FIELD = 'email' # поле имя будет заменяться на адрес, т.к. оно уникально
    REQUIRED_FIELDS = ['username'] # список имен полей при создании суперпользователя
