from django.db import models

# Create your models here.
class Singer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    NOT_SPECIFIED = 'N'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (NOT_SPECIFIED, 'Not Specified'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=NOT_SPECIFIED,
    )

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    duration = models.DurationField()

    def __str__(self):
        return self.title