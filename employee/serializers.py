from rest_framework import serializers

from main.models import EmployeeRequest


class EmployeeRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeRequest
        fields = ('id', 'asset_type', 'request_type', 'sender',
                  'quantity', 'urgency', 'status')
