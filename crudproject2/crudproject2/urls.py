from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddShowView.as_view(), name='addandshow'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name="deletedata"),
    path('<int:id>/', views.UserUpdateView.as_view(), name="updatedata"),
    path('user/', include('api.urls')),
]
