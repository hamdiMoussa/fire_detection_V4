from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('', views.home,name='home' ),
    path('about_us', views.about,name='about' ),

]