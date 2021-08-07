# from bookings.views import bookings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bookings(models.Model):
    title = models.CharField(max_length=200)
    field_name = models.EmailField()
    phone_number = models.CharField(max_length=200)
    body = models.TextField()
    geeks_field = models.DateField(max_length=100)
    geeks_field = models.TimeField(max_length=100)

  # field_name = models.DateField(auto)
    # field_name = models.TimeField()
    # time = models.TimeField(null=True)
    def __str__(self):
        return self.title

class Booking(models.Model):
    title = models.CharField(max_length=200)
    field_name = models.EmailField()
    phone_number = models.CharField(max_length=200)
    body = models.TextField()
    geeks_field = models.DateField(max_length=100)
    geeks_field = models.TimeField(max_length=100)

  # field_name = models.DateField(auto)
    # field_name = models.TimeField()
    # time = models.TimeField(null=True)
    def __str__(self):
        return self.title        