from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=30, verbose_name='страна', blank=True, null=True)

    activate_key = models.CharField(max_length=10, verbose_name='ключ активации', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []