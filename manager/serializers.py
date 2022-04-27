from rest_framework import serializers
from main.models import CompanyAsset


class CompanyAssetSerializer(serializers.ModelSerializer):
    '''
    Company asset serializer
    '''
    class Meta:
        model = CompanyAsset
        fields = '__all__'