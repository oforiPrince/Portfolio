from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='profile_pics', blank=True)
    carrier_summary = models.TextField(max_length=500)

    # Django stuff for authentication
    USERNAME_FIELD = "username"
    objects = AccountManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
