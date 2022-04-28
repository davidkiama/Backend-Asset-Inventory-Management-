from django.shortcuts import redirect, render
from pkg_resources import empty_provider

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

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


@api_view(['GET', 'POST', 'DELETE'])
def request_detail(request, pk):
    try:
        employee_request = EmployeeRequest.objects.get(pk=pk)
    except EmployeeRequest.DoesNotExist:
        return JsonResponse({'message': 'The Request does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        request_serializer = EmployeeRequestSerializer(employee_request)
        return JsonResponse(request_serializer.data)

    if request.method == "DELETE":
        employee_request.delete()
    return JsonResponse({'message': 'Request was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
