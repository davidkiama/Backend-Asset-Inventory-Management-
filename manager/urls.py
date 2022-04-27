from django.urls import path
from manager import views

urlpatterns = [
    path('dashboard', views.manager_dashboard, name='manager-dashboard'),
]