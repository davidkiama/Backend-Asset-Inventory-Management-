from rest_framework import serializers
from .models import User, ManagerProfile, EmployeeProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password',
                  'password2', 'manager', 'employee')

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            manager=self.validated_data['manager'],
            employee=self.validated_data['employee']

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords do not match.'})
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128)


class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = ('id', 'user', 'profile_photo',
                  'name', 'email', 'phone_number')


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ('id', 'user', 'profile_photo',
                  'name', 'email', 'phone_number')
