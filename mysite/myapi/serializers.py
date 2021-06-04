# serializers.py
from rest_framework import serializers

from .models import Trucks
from .models import Permit

class TrucksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trucks
        fields = ('id','vehicleNumber', 'vehicleStatus', 'vehicleGroup', 'totalPermits', 'ownerPhone', 'licenseStart', 'licenseEnd', 'licenseStatus', 'capacity', 'vehicleType', 'gpsIMEI', 'telecomProvider', 'simNo', 'registrationDate', 'installationtype', 'registrationBy')

class PermitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permit
        fields = ('id', 'PermitNumber', 'ILMS_number', 'VehicleNumber', 'PermitStart', 'PermitValidTill', 'LoadingLocation', 'Destination', 'Qty', 'Alerts')