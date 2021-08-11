from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import *

class Sliderimgform(forms.ModelForm):
    class Meta:
        model = Sliderimg
        fields = "__all__"

class sform(forms.ModelForm):
    class Meta:
        model = SlotBooking
        fields = "__all__"        