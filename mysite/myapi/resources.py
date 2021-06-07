from import_export import resources
from mysite.myapi.models import Trucks
from mysite.myapi.models import Permit
from mysite.myapi.models import User

class TruckResource(resources.ModelResource):
    class Meta:
        model = Trucks
class PermitResource(resources.ModelResource):
    class Meta:
        model = Permit
class UserResource(resources.ModelResource):
    class Meta:
        model = User