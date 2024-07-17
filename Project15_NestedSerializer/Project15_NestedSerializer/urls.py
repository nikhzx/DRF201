from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
# Create your views here.

router = DefaultRouter()

router.register('company', views.CompanyViewSet, basename='company')
router.register('device', views.DevicesViewSet, basename= 'device')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls, )),
    path('auth', include('rest_framework.urls', namespace= 'rest_framework'))
]
