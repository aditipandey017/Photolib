from django.contrib import admin
from django.urls import path
from . import views     #For linking the views.py file to the urls.py file



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home), 
    path('home/', views.home),     # This is the URL pattern for the home page
    path('gallery/', views.gallery),        # This is the URL pattern for the gallery page
    path('add/', views.add),
    path('upload/', views.upload, name='upload'),
    path('show_uploaded_image/', views.show_uploaded_image, name='show_uploaded_image'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('search/', views.search, name='search'),
    
      
]