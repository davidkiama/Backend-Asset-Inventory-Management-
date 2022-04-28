from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    manager = models.BooleanField('Manager', default=False)
    employee = models.BooleanField('Employee', default=False)


class ManagerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    profile_photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    email = models.EmailField()


class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    profile_photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    email = models.EmailField()
