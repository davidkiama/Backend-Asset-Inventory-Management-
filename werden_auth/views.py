from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, ManagerProfile, EmployeeProfile
from .serializers import RegistrationSerializer, LoginSerializer, ManagerProfileSerializer, EmployeeProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

# Create your views here.


def index(request):
    return render(request, 'index.html')


class RegistrationView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializers = RegistrationSerializer(users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():

            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user).key
            data['token'] = token

        else:
            data = serializer.errors
        return Response(data)


def check_user_acc(request):
    tokens = Token.objects.filter(user=request.user)
    for token in tokens:
        user = Token.objects.get(key=token).user

    return user.manager


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)

            user_manager = Token.objects.get(key=token).user.manager
            if user_manager:
                user_role = 'Manager'
            else:
                user_role = 'Employee'

            data['token'] = token.key
            data['User_role'] = user_role

        else:
            data = serializer.errors

        return Response(data)


class LogoutView(APIView):
    def get(self, request, format=None):
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': ('User logged out.')}
        return Response(content)


class ManagerProfileView(APIView):
    def get(self, request, format=None):
        profiles = ManagerProfile.objects.all()
        serializers = ManagerProfileSerializer(profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ManagerProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeProfileView(APIView):
    def get(self, request, format=None):
        profiles = EmployeeProfile.objects.all()
        serializers = EmployeeProfileSerializer(profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = EmployeeProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
