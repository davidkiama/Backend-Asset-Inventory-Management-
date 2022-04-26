from urllib import request
from django.db import models

# Create your models here.


class Asset(models.Model):
    # creator = models.ForeignKey('manager', on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()


class EmployeeRequest (models.Model):
    # sender = models.ForeignKey('employee', on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=50)
    request_type = models.CharField(max_length=50)
    urgency = models.CharField(max_length=50)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)

    def save_request(self):
        self.save()
