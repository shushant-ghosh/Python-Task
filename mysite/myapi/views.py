from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TrucksSerializer
from .serializers import PermitSerializer
from .models import Trucks
from .models import Permit


class TrucksViewSet(viewsets.ModelViewSet):
    queryset = Trucks.objects.all().order_by('id')
    serializer_class = TrucksSerializer

class PermitViewSet(viewsets.ModelViewSet):
    queryset = Permit.objects.all().order_by('id')
    serializer_class = PermitSerializer
