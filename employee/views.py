from django.shortcuts import redirect, render

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import EmployeeRequestSerializer
from main.models import EmployeeRequest

# Create your views here.


class EmployeeRequestViewset(viewsets.ModelViewSet):
    queryset = EmployeeRequest.objects.all()
    serializer_class = EmployeeRequestSerializer

    def post(self, request, format=None):
        serializers = EmployeeRequestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


def create_request(request):
    # Check if user sending the request if of type employee

    # Create request
    if request.method == 'POST':

        asset_type = request.POST['asset_type']
        request_type = request.POST['request_type']
        urgency = request.POST['urgency']
        quantity = request.POST['quantity']
        description = request.POST['description']

        new_request = EmployeeRequest(
            asset_type=asset_type, request_type=request_type, urgency=urgency, quantity=quantity, status='open')

        new_request.save_request()
        print('Request saved to the DB')

        return redirect(create_request)
    return render(request, 'create_request.html')


def employee_dashboard(request):
    employee_requests = EmployeeRequest.objects.all()

    return render(request, 'dashboard.html', {'employee_requests': employee_requests})
