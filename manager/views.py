from urllib import response
from django.shortcuts import render
from main.models import CompanyAsset
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CompanyAssetSerializer

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

class CompanyAssetsData(APIView):
    '''
    Class that handles company assets apis
    '''
    def get(self, request, format=None):
        '''
        Get function that display company assets data in JSON
        '''
        company_assets = CompanyAsset.objects.all().order_by('asset_name')
        assets_serializer = CompanyAssetSerializer(company_assets, many=True)
        return Response(assets_serializer.data)

    def post(self, request, format=None):
        '''
        Post function that handles company assets data in JSON
        '''
        assets_serializer =CompanyAssetSerializer(data=request.data)
        if assets_serializer.is_valid():
            assets_serializer.save()
            return Response(assets_serializer.data, status=status.HTTP_201_CREATED)
        return Response(assets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



