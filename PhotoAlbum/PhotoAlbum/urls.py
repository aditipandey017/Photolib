"""
URL configuration for PhotoAlbum project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
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


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)