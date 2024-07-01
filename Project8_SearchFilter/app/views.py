from urllib import request
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city']
    search_fields = ['^city']
    