
from django.shortcuts import render
from main.models import CompanyAsset
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CompanyAssetSerializer
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse

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
        try:
            token, created = Token.objects.get_or_create(user=request.user)
            user_obj = Token.objects.get(key=token).user

        except:

            return JsonResponse({'message': 'You must be logged in to view company assets'}, status=status.HTTP_401_UNAUTHORIZED) 
        
        if user_obj.manager:
            company_assets = CompanyAsset.objects.all()
            assets_serializer = CompanyAssetSerializer(company_assets, many=True)
        else:
            return JsonResponse({'message': 'You must be logged in to view company assets'}, status=status.HTTP_401_UNAUTHORIZED)             

        if user_obj.manager:
            company_assets = CompanyAsset.objects.all()
            assets_serializer = CompanyAssetSerializer(
                company_assets, many=True)
        else:
            return JsonResponse({'message': 'You must be logged in to view company assets'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(assets_serializer.data)

    def post(self, request, format=None):
        '''
        Post function that handles company assets data in JSON
        '''
        try:
            token, created = Token.objects.get_or_create(user=request.user)
            user_obj = Token.objects.get(key=token).user


        except:
            return JsonResponse({'message': 'You must be logged in to create company assets'}, status=status.HTTP_401_UNAUTHORIZED) 

        assets_serializer =CompanyAssetSerializer(data=request.data)
        if assets_serializer.is_valid():
            assets_serializer.save()
            return Response(assets_serializer.data, status=status.HTTP_201_CREATED)

        except:
            return JsonResponse({'message': 'You must be logged in to create company assets'}, status=status.HTTP_401_UNAUTHORIZED)

        if user_obj.manager:
            assets_serializer = CompanyAssetSerializer(data=request.data)
            if assets_serializer.is_valid():
                assets_serializer.save()
                return Response(assets_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'You must be a manager to create company assets'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, format=None):
        '''
        Put function that handles company assets details update
        '''
        try:
            token, created = Token.objects.get_or_create(user=request.user)
            user_obj = Token.objects.get(key=token).user

        except:
            return JsonResponse({'message': 'You must be logged in to approve/reject company assets'}, status=status.HTTP_401_UNAUTHORIZED) 
        return Response()



