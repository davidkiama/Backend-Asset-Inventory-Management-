from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    username=models.CharField(max_length=60,unique=True)
    email=models.EmailField(unique=True)
    manager=models.BooleanField('Manager',default=False)
    employee=models.BooleanField('Employee',default=False)

class ManagerProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    profile_photo=models.ImageField(upload_to = 'images/')
    name=models.CharField(max_length =100)
    email=models.EmailField()
    phone_number=models.IntegerField()

class EmployeeProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    profile_photo=models.ImageField(upload_to = 'images/')
    name=models.CharField(max_length =100)
    email=models.EmailField()
    phone_number=models.IntegerField()