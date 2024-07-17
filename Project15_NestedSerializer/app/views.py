from .models import Company, Device
from .serializers import CompanySerializer, DevicesSerializer
from rest_framework import viewsets

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DevicesSerializer
