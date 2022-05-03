from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('manager/profile/', views.ManagerProfileView.as_view()),
    path('employee/profile/', views.EmployeeProfileView.as_view()),
]
