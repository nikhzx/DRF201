from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from .mypagination import MyCursorPagination
# Create your views here.

class StudentListAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination