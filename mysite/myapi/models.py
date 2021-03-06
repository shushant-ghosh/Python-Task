from django.db import models
class Trucks(models.Model):
    vehicleNumber = models.CharField(max_length=60)
    vehicleStatus = models.CharField(max_length=60)
    vehicleGroup = models.CharField(max_length=60)
    totalPermits = models.CharField(max_length=60)
    ownerPhone = models.CharField(max_length=60)
    licenseStart = models.CharField(max_length=60)
    licenseEnd = models.CharField(max_length=60)
    licenseStatus = models.CharField(max_length=60)
    capacity = models.CharField(max_length=60)
    vehicleType = models.CharField(max_length=60)
    gpsIMEI = models.CharField(max_length=60)
    telecomProvider = models.CharField(max_length=60)
    simNo = models.CharField(max_length=60)
    registrationDate = models.CharField(max_length=60)
    installationtype = models.CharField(max_length=60)
    registrationBy = models.CharField(max_length=60)

   
    class Meta:
        db_table = "myapi_trucks"


class Permit(models.Model):
    PermitNumber = models.CharField(max_length=60)	
    ILMS_number = models.CharField(max_length=60)	
    VehicleNumber = models.CharField(max_length=60)	
    PermitStart = models.CharField(max_length=60)	
    PermitValidTill = models.CharField(max_length=60)	
    LoadingLocation = models.CharField(max_length=60)	
    Destination = models.CharField(max_length=60)	
    Qty = models.CharField(max_length=60)	
    Alerts = models.CharField(max_length=60)
   
    class Meta:
        db_table = "myapi_permit"

class User(models.Model):
    name =  models.CharField(max_length=60)
    email =  models.CharField(max_length=60)
    phonenumber =  models.CharField(max_length=60)

    class Meta:
        db_table = "myapi_user"
