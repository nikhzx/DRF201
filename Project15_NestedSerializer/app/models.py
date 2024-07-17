from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length = 50)

    MOBILE = 'Mobile Phone'
    TABLET = 'Tablet'
    WATCH = 'Smart Watch'
    NOT_SPECIFIED = 'Not Specified'

    DEVICE_CHOICES = [
        (MOBILE, 'Mobile Phone'),
        (TABLET, 'Tablet'),
        (WATCH, 'Smart Watch'),
        (NOT_SPECIFIED, 'Not Specified')
    ]
    type = models.CharField(
        max_length = 50,
        choices = DEVICE_CHOICES,
        default = NOT_SPECIFIED,)
    
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name = 'devices')
    price = models.FloatField()

    def __str__(self):
        return self.name