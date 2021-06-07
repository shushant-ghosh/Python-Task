from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import TrucksSerializer
from .serializers import PermitSerializer
from .serializers import UserSerializer
from .models import Trucks
from .models import Permit
from .models import User

class TrucksViewSet(viewsets.ModelViewSet):
    queryset = Trucks.objects.all().order_by('id')
    serializer_class = TrucksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicleNumber', 'gpsIMEI', 'vehicleGroup', 'vehicleType', 'licenseEnd']

class PermitViewSet(viewsets.ModelViewSet):
    queryset = Permit.objects.all().order_by('id')
    serializer_class = PermitSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(User, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def createUser(request):
    user = User.objects.create_user('sg', 'lennon@thebeatles.com', 'India@123')

    user.last_name = 'Lennon'
    user.save()
    return user

