from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
    path('api/manager/profile/', views.ManagerProfileView.as_view()),
    path('api/employee/profile/', views.EmployeeProfileView.as_view()),
]