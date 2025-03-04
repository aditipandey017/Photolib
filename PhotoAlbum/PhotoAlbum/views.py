from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def home(request):
    # return HttpResponse("Hello world! This is my home page.")
    return render(request, 'home.html')    # This will render the home.html template

def gallery(request):
    # return HttpResponse("This is the about page.")
    return render(request, 'gallery.html')    # This will render the gallery.html template


def add(request):
   
    return render(request, 'add.html')    # This will render the add.html template

def upload(request):
   
    return render(request, 'upload.html') 

def upload(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        description = request.POST.get('description')
        category = request.POST.get('category')

        # Save the uploaded file using FileSystemStorage
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)  # Get the file URL

        request.session['uploaded_image'] = {
            'image_url': image_url,
            'description': description,
            'category': category
        }

        return redirect('show_uploaded_image')  # Redirect to the view that shows the uploaded image

    return render(request, 'add.html')

def show_uploaded_image(request):
    uploaded_image = request.session.get('uploaded_image', None)
    return render(request, 'upload.html', {'uploaded_image': uploaded_image})


def about(request):
   
    return render(request, 'about.html') 

def contact(request):
   
    return render(request, 'contact.html') 

def search(request):
    return HttpResponse("This is the search page.")
