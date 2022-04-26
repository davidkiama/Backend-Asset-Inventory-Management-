
from django.contrib import admin
from django.urls import path, include

from employee.views import EmployeeRequestViewset

from rest_framework import routers
router = routers.DefaultRouter()


router.register('', EmployeeRequestViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include(router.urls)),
    path('employee/', include('employee.urls'))
]
