from django.contrib import admin
from .models import User,ManagerProfile,EmployeeProfile

# Register your models here.
admin.site.register(User)
admin.site.register(ManagerProfile)
admin.site.register(EmployeeProfile)

