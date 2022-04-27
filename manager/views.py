from django.shortcuts import render
from main.models import CompanyAsset

# Create your views here.
def manager_dashboard(request):
    '''
    Manager's dashboard view function
    '''
    company_assets = CompanyAsset.objects.all()

    context = {
        'companyAssets':company_assets
    }
    return render(request, 'manager/dashboard_manager.html', context)


