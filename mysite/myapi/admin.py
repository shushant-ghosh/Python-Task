from django.contrib import admin
from .models import Trucks
from .models import Permit
from .models import User
from import_export.admin import ImportExportModelAdmin

@admin.register(Trucks)
class TruckAdmin(ImportExportModelAdmin):
    list_display = ('vehicleNumber', 'vehicleStatus', 'vehicleGroup', 'totalPermits', 'ownerPhone', 'licenseStart', 'licenseEnd', 'licenseStatus', 'capacity', 'vehicleType', 'gpsIMEI', 'telecomProvider', 'simNo', 'registrationDate', 'installationtype', 'registrationBy')
    pass
@admin.register(Permit)
class PermitAdmin(ImportExportModelAdmin):
    list_display = ('PermitNumber', 'ILMS_number', 'VehicleNumber', 'PermitStart', 'PermitValidTill', 'LoadingLocation', 'Destination', 'Qty', 'Alerts')
    pass
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'phonenumber')
    pass
