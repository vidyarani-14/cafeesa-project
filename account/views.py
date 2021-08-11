from account.forms import Sliderimgform, sform
from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from .models import SlotBooking, Sliderimg,test,test_2,test_1
from django.contrib import auth
from django.contrib.auth.models import User
from .models import  *



def index(request):
    s=Sliderimg.objects
    t=test.objects
    t1=test_1.objects
    t2=test_2.objects
    if request.method == 'POST':
          s = SlotBooking()
          s.image = request.POST.get ('image')
          s.title = request.POST.get('title')
          s.body = request.POST.get ('body')
          s.pub_date = request.POST.get ('pub_date')
         
          s.save()
          return redirect ('index')
    else:

     return render (request,"cafeesa/index.html",{'s': s,'t':t,'t1':t1,'t2': t2})
        
  
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
    t=test.objects
    t1=test_1.objects
    t2=test_2.objects   
    return render(request, 'cafeesa/testimonial.html',{"t": t,'t1': t1,'t2': t2}) 

def error(request):
    return render(request, 'pluto-html/404_error.html') 

def calendar(request):
    return render(request, 'pluto-html/calendar.html')   

def charts(request):
    return render(request, 'pluto-html/charts.html')  
    


@login_required(login_url='/login_1/')
def bookings(request):  
    
     return render(request, 'pluto-html/bookings.html',{"context":SlotBooking.objects.all()})     
    
@login_required( login_url="cafeesa/login_1.html")
  
def dashboard_2(request):
    return render(request, 'pluto-html/dashboard_2.html')              

@login_required(login_url='/login_1/')
def dashboard(request):
    return render(request, 'pluto-html/dashboard.html') 

def email(request):
    return render(request, 'pluto-html/email.html')  

def general_elements(request):
    return render(request, 'pluto-html/general_elements.html')      

def icons(request):
    return render(request, 'pluto-html/icons.html')                

@login_required(login_url='/login_1/')
def index_1(request):
    return render(request, 'pluto-html/index_1.html')     

def invoice(request):
    return render(request, 'pluto-html/invoice.html')      


# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             return render(request, 'account/login.html',{'error':'username or password is incorrect.'})
#     else:
        
#       return render(request, 'pluto-html/login.html')       

def map(request):
    return render(request, 'pluto-html/map.html')   

def edit(request,id):
    get_id = Sliderimg.objects.get(id = id)
    forms = Sliderimgform(request.POST or None, request.FILES or None, instance=get_id)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect('Sliderimage') 
            
    return render(request, 'pluto-html/edit.html',{'s': Sliderimg.objects.all(),'form': forms}) 


def edit_1(request,id):
    get_id = SlotBooking.objects.get(id = id)
    forms = sform(request.POST or None, request.FILES or None, instance=get_id)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect('bookings') 
            
    return render(request, 'pluto-html/edit_1.html',{'s': SlotBooking.objects.all(),'form': forms}) 



def add(request):
    
    forms_ = Sliderimgform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if forms_.is_valid():
            forms_.save()
            return redirect(Sliderimage)
    return render(request, 'pluto-html/add.html',{'s': Sliderimg.objects.all(),'form': forms_})  

def add_1(request):
    
    forms_ = sform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if forms_.is_valid():
            forms_.save()
            return redirect(bookings)
    return render(request, 'pluto-html/add_1.html',{'s': SlotBooking.objects.all(),'form': forms_})      
            






def update(request):
    s = Sliderimg.objects.get(pk=id)
    form = Sliderimgform(request.POST,instance = s)
    if form.is_valid():
        form.save()
        s = Sliderimg.objects.all()
        return redirect(Sliderimage,{'s':s})


def update_1(request):
    s = SlotBooking.objects.get(pk=id)
    form = sform(request.POST,instance = s)
    if form.is_valid():
        form.save()
        s = SlotBooking.objects.all()
        return redirect(bookings,{'s':s})        
      


def delete(request,id):
    get_id = Sliderimg.objects.get(id=id)
    get_id.delete ()
    return redirect (Sliderimage)



def delete_1(request,id):
    get_id = SlotBooking.objects.get(id=id)
    get_id.delete ()
    return redirect (bookings)    
   


def media_gallery(request):
    return render(request, 'pluto-html/media_gallery.html')   

def price(request):
    return render(request, 'pluto-html/price.html')     

@login_required(login_url='/login_1/')
def profile(request):
    return render(request, 'pluto-html/profile.html')  

def project(request):
    return render(request, 'pluto-html/project.html') 

@login_required(login_url='/login_1/')
def settings(request):
    return render(request, 'pluto-html/settings.html')     

def tables(request):
    return render(request, 'pluto-html/tables.html')  

@login_required(login_url='/login_1/')
def Sliderimage(request):
    s=Sliderimg.objects
    return render(request, 'pluto-html/Sliderimage.html',{'s': s})            

@login_required(login_url='/login_1/')
def testimonial_1(request):
    s=Sliderimg.objects
    t=test.objects
    t1=test_1.objects
    t2=test_2.objects
    return render(request, 'pluto-html/testimonial_1.html',{'s': s,'t':t,'t1':t1,'t2': t2})

def login_1(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index_1')
        else:
            return render(request, 'cafeesa/login_1.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'cafeesa/login_1.html')


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('index')
        else:
            return render(request, 'cafeesa/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'cafeesa/signup.html')    

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')   
         
    else:
        return render(request, 'cafeesa/login_1.html')        