from urllib import request
from django.db import models

from werden_auth.models import User

# Create your models here.


class CompanyAsset(models.Model):
    creator = models.CharField(max_length=50, default='manager')
    asset_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.asset_name


class EmployeeRequest(models.Model):
    sender = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=50)
    request_type = models.CharField(max_length=50)
    urgency = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def save_request(self):
        self.save()
