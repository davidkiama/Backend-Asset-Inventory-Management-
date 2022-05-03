
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('werden_auth.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('manager/', include('manager.urls')),
    path('requests/', include('employee.urls')),
    path('auth/', include('werden_auth.urls')),
]
