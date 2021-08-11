"""cafeesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from account import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index' ),
    path('about/',views.about, name='about' ),
    path('book/',views.book, name='book' ),
    path('testimonial/',views.testimonial, name='testimonial' ),


    path('update/<int:id>',views.update, name='update' ), 
    path('edit/<int:id>',views.edit, name='edit' ), 
    path('delete/<int:id>',views.delete, name='delete' ),
    path('add/',views.add, name='add' ),
    path('404_error/',views.error, name='404_error' ),
    path('calendar/',views.calendar, name='calendar' ),
    path('charts/',views.charts, name='charts' ),
    path('bookings/',views.bookings, name='bookings' ),
    path('dashboard_2/',views.dashboard_2, name='dashboard_2' ),
    path('dashboard/',views.dashboard, name='dashboard' ),
    path('email/',views.email, name='email' ),
    path('general_elements/',views.general_elements, name='general_elements' ),
    path('icons/',views.icons, name='icons' ),
    path('index_1/',views.index_1, name='index_1' ),
    path('invoice/',views.invoice, name='invoice' ),

    path('map/',views.map, name='map' ),
    path('media_gallery/',views.media_gallery, name='media_gallery' ),
    path('price/',views.price, name='price' ),
    path('profile/',views.profile, name='profile' ),
    path('project/',views.project, name='project' ),
    path('settings/',views.settings, name='settings' ),
    path('tables/',views.tables, name='tables' ),
    path('Sliderimage/',views.Sliderimage, name='Sliderimage' ),
    path('testimonial_1/',views.testimonial_1, name='testimonial_1' ),
    path('update_1/<int:id>',views.update_1, name='update_1' ), 
    path('edit_1/<int:id>',views.edit_1, name='edit_1' ), 
    path('delete_1/<int:id>',views.delete_1, name='delete_1' ),
    path('add_1/',views.add_1,name='add_1'),
    path('login_1/',views.login_1,name='login_1'),
    path('signup/',views.signup,name='signup'),
    path('logout', views.logout, name='logout' )





    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

