from urllib import request
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1')
    serializer_class = StudentSerializer
    filterset_fields = ['city', 'passby']
    filter_backends = [DjangoFilterBackend]
    