from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User,ManagerProfile,EmployeeProfile
from .serializers import RegistrationSerializer,LoginSerializer,ManagerProfileSerializer,EmployeeProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from django.contrib.auth import authenticate
from django.http  import Http404

# Create your views here.

def index(request):
    return render(request, 'index.html')

class RegistrationView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        users=User.objects.all()
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

class LoginView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key

        else:
            data = serializer.errors

        return Response(data)

class LogoutView(APIView):
    def get(self, request, format=None):
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': ('User logged out.')}
        return Response(content, status=status.HTTP_200_OK)
        

class ManagerProfileView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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

class ManagerProfileDescription(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_profile(self, id):
        try:
            return ManagerProfile.objects.get(id=id)
        except ManagerProfile.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        manager_profile = self.get_profile(id)
        serializers = ManagerProfileSerializer(manager_profile)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        manager_profile = self.get_profile(id)
        serializers = ManagerProfileSerializer(manager_profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeProfileView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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

class EmployeeProfileDescription(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_profile(self, id):
        try:
            return EmployeeProfile.objects.get(id=id)
        except EmployeeProfile.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        employee_profile = self.get_profile(id)
        serializers = EmployeeProfileSerializer(employee_profile)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        employee_profile = self.get_profile(id)
        serializers = EmployeeProfileSerializer(employee_profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
