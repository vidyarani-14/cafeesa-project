from django.contrib import admin

# Register your models here.


from .models import SlotBooking
from .models import Sliderimg

# Register your models here.
admin.site.register(SlotBooking)
admin.site.register(Sliderimg)

