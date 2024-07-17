from django.contrib import admin
from .models import Device, Company
# Register your models here.

@admin.register(Device)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'company','price']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']