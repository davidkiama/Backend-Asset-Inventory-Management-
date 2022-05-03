from django.db import models

# Create your models here.


class CompanyAsset(models.Model):
    creator = models.CharField(max_length=50, default='manager')
    asset_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.asset_name

class EmployeeRequest (models.Model):
    # sender = models.ForeignKey('employee', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    urgenty = models.CharField(max_length=50)
    quantity = models.IntegerField()
