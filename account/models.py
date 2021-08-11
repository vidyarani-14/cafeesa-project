from django.db import models

# Create your models here.


from django.contrib.auth.models import User

# Create your models here.
class SlotBooking(models.Model):
    title = models.CharField(max_length=30,null=True)
    email_field = models.EmailField(null=True)
    phone_number = models.CharField(max_length=10,null=True)
    geeks_field = models.DateField(max_length=100,null=True)
    geeks_field = models.TimeField(max_length=100,null=True)
    body = models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.title

class Sliderimg(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField()
  
  
class test(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    body = models.TextField()

class test_1(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    body = models.TextField()

class test_2(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    body = models.TextField()    