from accounts.models import SlotBooking
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from .models import  *



def index(request):
    return render(request, 'cafeesa/index.html')

def about(request):
    return render(request, 'cafeesa/about.html')

def book(request):
    if request.method == 'POST':
        product = SlotBooking()
        product.first_name = request.POST.get ('first_name')
        product.email_field = request.POST.get('email_field')
        product.phone_number = request.POST.get ('phone_number')
        product.geeks_field = request.POST.get ('geeks_field')
        product.geeks_field = request.POST.get('geeks_field')
        product.body = request.POST.get ('body')
        product.save()
        return redirect ('index')
    else:

        return render (request,"cafeesa/book.html",{"context":SlotBooking.objects.all()})

        

    # if request.method == 'POST':
    #   form = bform(request.POST )
    #   if form.is_valid():
    #     form.save()
    #   return render(request, "cafeesa/book.html")
      
    # form = bform()
    # context = {'form' : form}
    # return render(request, 'cafeesa/book.html',context)

    # if request.method == 'POST':
    #    form = bform(request.POST,)
    #    if form.is_valid():
    #         form.save()
    # form = bform()
    # return render(request, "cafeesa/book.html", {'form': form})


def testimonial(request):
    return render(request, 'cafeesa/testimonial.html') 

def error(request):
    return render(request, 'pluto-html/404_error.html') 

def calendar(request):
    return render(request, 'pluto-html/calendar.html')   

def charts(request):
    return render(request, 'pluto-html/charts.html')  

def bookings(request):
    #  if request.method == 'POST':
    #     user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
    #     if user is not None:
    #         auth.admin(request, user)
    #         return redirect('')
    #     else:
    #      return render(request, 'admin',{'error':'username or password is incorrect.'})
    #  else:
    #   return render(request,'admin')  
    
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
