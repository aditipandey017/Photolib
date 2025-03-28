from django.contrib import admin
from django.urls import path
from . import views     #For linking the views.py file to the urls.py file
from .models import Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'message')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
