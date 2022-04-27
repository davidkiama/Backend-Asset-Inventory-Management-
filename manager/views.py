from django.shortcuts import render

# Create your views here.
def manager_dashboard(request):
    '''
    Manager's dashboard view function
    '''
    return render(request, 'manager/dashboard_manager.html')