from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet

router = DefaultRouter()

router.register('crud', UserViewSet, basename='Lollipop')

urlpatterns = [
    path('', include(router.urls), name='user_api'),
]