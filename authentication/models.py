from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)'''

        user = self.create_user(
            email,password,**extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

