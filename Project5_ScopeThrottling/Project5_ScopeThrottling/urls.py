from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/", views.StudentList.as_view()),
    path("studentapi/<int:pk>", views.StudentRetrieve.as_view()),
]
