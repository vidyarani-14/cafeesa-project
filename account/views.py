from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from .models import SlotBooking, Sliderimg

from django.contrib import auth
from django.contrib.auth.models import User
from .models import  *



def index(request):
    if request.method == 'POST':
        s = Sliderimg()
        s.title = request.POST.get ('title')
        s.body = request.POST.get('body')
        s.pub_date = request.POST.get ('pub_date')
        s.image = request.POST.get('image')
        s.save()
        return redirect ('index')
    else:

        return render (request,"cafeesa/index.html")
        
  
def about(request):
    return render(request, 'cafeesa/about.html')

def book(request):
    if request.method == 'POST':
         product = SlotBooking()
         product.title = request.POST.get ('title')
         product.email_field = request.POST.get('email_field')
         product.phone_number = request.POST.get ('phone_number')
         product.geeks_field = request.POST.get ('geeks_field')
         product.geeks_field = request.POST.get('geeks_field')
         product.body = request.POST.get ('body')
         product.save()
         return redirect ('index')
    else:

        return render (request,"cafeesa/book.html",{"context":SlotBooking.objects.all()})


def testimonial(request):
    return render(request, 'cafeesa/testimonial.html') 

def error(request):
    return render(request, 'pluto-html/404_error.html') 

def calendar(request):
    return render(request, 'pluto-html/calendar.html')   

def charts(request):
    return render(request, 'pluto-html/charts.html')  
    

@login_required( login_url="/cafeesa/pluto-html/login")
def bookings(request):  
     return render(request, 'pluto-html/bookings.html',{"context":SlotBooking.objects.all()})     
    
  
def dashboard_2(request):
    return render(request, 'pluto-html/dashboard_2.html')              

def dashboard(request):
    return render(request, 'pluto-html/dashboard.html') 

def email(request):
    return render(request, 'pluto-html/email.html')  

def general_elements(request):
    return render(request, 'pluto-html/general_elements.html')      

def icons(request):
    return render(request, 'pluto-html/icons.html')                

def index_1(request):
    return render(request, 'pluto-html/index_1.html')     

def invoice(request):
    return render(request, 'pluto-html/invoice.html')      

@permission_required ('user.is_superuser')
def login(request):


    return render(request, 'pluto-html/login.html')       

def map(request):
    return render(request, 'pluto-html/map.html')   

def media_gallery(request):
    return render(request, 'pluto-html/media_gallery.html')   

def price(request):
    return render(request, 'pluto-html/price.html')     

def profile(request):
    return render(request, 'pluto-html/profile.html')  

def project(request):
    return render(request, 'pluto-html/project.html') 

def settings(request):
    return render(request, 'pluto-html/settings.html')     

def tables(request):
    return render(request, 'pluto-html/tables.html')  

def widgets(request):
    return render(request, 'pluto-html/widgets.html')            
