from urllib import request
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1')
    serializer_class = StudentSerializer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby = user)
    