from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

#Creating Router Object
router = DefaultRouter()

#Register StudentViewSet with Router
router.register('studentapi',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'), name='rest'),
]
