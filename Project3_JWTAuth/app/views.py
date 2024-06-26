from requests import Session
from .custompermissions import MyPermission
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

#this Provides Read-only operations to perform
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #AUTH AND PERMISSION for Class View
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    # permission_classes = [MyPermission]

    #CustomPermission
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]