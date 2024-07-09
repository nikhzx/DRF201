from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class MyPageNumPagination(PageNumberPagination):
    page_size = 5          #num of record per page
    page_query_param = 'num' #keyword for page in url
    page_size_query_param = 'records' #ClientSide control of num of records
    max_page_size = 6          #Controls the max record side
    last_page_strings = 'end'  #gives last page records
    all_query_param = 'all' 

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get(self.all_query_param):
            return None  # Disables pagination
        return super().paginate_queryset(queryset, request, view)

class StudentListAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumPagination