from .models import Company, Device
from rest_framework import serializers

class DevicesSerializer(serializers.ModelSerializer):
    # company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    company = serializers.SlugRelatedField(queryset=Company.objects.all(), slug_field='country')
    class Meta:
        model = Device
        fields = ['id', 'name', 'type', 'company', 'price']

class CompanySerializer(serializers.ModelSerializer):
    # device = serializers.StringRelatedField(many=True, read_only=True)
    devices = DevicesSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'devices', 'country']
