
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .serializers import EmployeeRequestSerializer
from main.models import EmployeeRequest


from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['GET', 'POST'])
def request_list(request):

    try:
        token, created = Token.objects.get_or_create(user=request.user)
        user_obj = Token.objects.get(key=token).user

    except:
        return JsonResponse({'message': 'You must be logged in to view requests'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':

        # If logged user is emloyee, show only his requests
        if user_obj.employee:
            employee_requests = EmployeeRequest.objects.filter(
                sender=user_obj.username)
        else:
            # If logged user is manager show all requests
            employee_requests = EmployeeRequest.objects.all()

        employee_req_serializer = EmployeeRequestSerializer(
            employee_requests, many=True)

        return JsonResponse(employee_req_serializer.data, safe=False)

     # POST single object
    if request.method == 'POST':
        if user_obj.employee:
            # set sender to the user obj
            request.data['sender'] = user_obj.username
        else:
            return JsonResponse({'message': 'You must be an employee to create requests'}, status=status.HTTP_401_UNAUTHORIZED)

        serializers = EmployeeRequestSerializer(data=request.data)
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def request_detail(request, pk):
    try:
        token, created = Token.objects.get_or_create(user=request.user)
        user_obj = Token.objects.get(key=token).user

    except:
        return JsonResponse({'message': 'You must be logged in to view requests'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        employee_request = EmployeeRequest.objects.get(pk=pk)
    except EmployeeRequest.DoesNotExist:
        return JsonResponse({'message': 'The Request does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET single object
    if request.method == 'GET':
        request_serializer = EmployeeRequestSerializer(employee_request)
        return JsonResponse(request_serializer.data)

    # DELETE single object
    if request.method == "DELETE":
        employee_request.delete()
    return JsonResponse({'message': 'Request was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
