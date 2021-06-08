from django.test import TestCase
from ..models import Trucks, Permit
# Create your tests here.

class TrucksTest(TestCase):
    def setUp(self):
        Trucks.object.create(
            vehicleNumber = 'UP70QR4230',
            vehicleStatus = 'Idle',
            vehicleGroup = 'DMG',
            totalPermits = '20',
            ownerPhone = '9935748817',
            licenseStart = '20-01-2021 21:14',
            licenseEnd = '25-01-2022 21:51',
            licenseStatus = 'Active',
            capacity = '17',
            vehicleType = 'Tipper',
            gpsIMEI = '354018110121609',
            telecomProvider = 'Airtel',
            simNo = '8296948937',
            registrationDate = '07-02-2021',
            installationtype = 'New Installation',
            registrationBy = 'Admin',
        )
    
    def testTruck(self):
        trucks_tipper = Trucks.objects.get(vehicleType='Tipper')
        self.assertEqual(
            trucks_tipper.get_Type(), "It is a Tipper truck")

class PermitTest(TestCase):
    def setUp(self):
        Permit.object.create(
            PermitNumber = 'GBL567572',
    ILMS_number = '60333029',
    VehicleNumber = 'KA58B9742',
    PermitStart = '09-02-2021 08:12',
    PermitValidTill = '09-02-2021 16:55',
    LoadingLocation = 'OMSSMP',
    Destination = 'Kanakapura',
    Qty = '12.3',
    Alerts = '1',
        )
    
    def permitTruck(self):
        permit_destination = Permit.objects.get(Destination='Kanakapura')
        self.assertEqual(
            permit_destination.get_destination(), "Destination is Kanakapura")