from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

class MyLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 7
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'

    # def paginate_queryset(self, queryset, request, view=None):
    #     if request.query_params.get(self.all_query_param):
    #         return None  # Disables pagination
    #     return super().paginate_queryset(queryset, request, view)

class StudentListAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination