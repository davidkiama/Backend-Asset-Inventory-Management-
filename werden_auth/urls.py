from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('accounts/register/', views.RegistrationView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('manager/profile/', views.ManagerProfileView.as_view()),
    path('employee/profile/', views.EmployeeProfileView.as_view()),
    path('api/manager_profile/manager_profile-id/<int:id>/',views.ManagerProfileDescription.as_view()),
    path('api/employee_profile/employee_profile-id/<int:id>/',views.EmployeeProfileDescription.as_view()),
]