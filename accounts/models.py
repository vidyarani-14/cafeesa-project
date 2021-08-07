
from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class SlotBooking(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    email_field = models.EmailField(null=True)
    phone_number = models.CharField(max_length=10,null=True)
    geeks_field = models.DateField(max_length=100,null=True)
    geeks_field = models.TimeField(max_length=100,null=True)
    body = models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.body
