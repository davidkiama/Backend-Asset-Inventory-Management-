from django.shortcuts import redirect, render

from main.models import EmployeeRequest

# Create your views here.


def create_request(request):
    # Check if user sending the request if of type employee
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
