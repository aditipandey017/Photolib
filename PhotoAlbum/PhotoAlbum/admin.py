from django.contrib import admin
from django.urls import path
from . import views     #For linking the views.py file to the urls.py file
from .models import contact

admin.site.register(contact)
