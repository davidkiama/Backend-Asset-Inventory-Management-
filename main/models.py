from django.db import models

# Create your models here.


class Asset(models.Model):
    creator = models.ForeignKey('manager', on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()


class Request (models.Model):
    sender = models.ForeignKey('employee', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    urgenty = models.CharField(max_length=50)
    quantity = models.IntegerField()
