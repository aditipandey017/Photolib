from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Contact

def home(request):
    # return HttpResponse("Hello world! This is my home page.")
    return render(request, 'home.html')    # This will render the home.html template

def gallery(request):
    # return HttpResponse("This is the about page.")
    return render(request, 'gallery.html')    # This will render the gallery.html template


def add(request):   
    return render(request, 'add.html')    # This will render the add.html template


def upload(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        category = request.POST.get('category')
        description = request.POST.get('description')
        

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)  
        request.session['uploaded_image'] = {
                    'image_url': image_url,
                    'description': description,
                    'category': category
                }

        return redirect('show_uploaded_image')  

    return render(request, 'upload.html')

def show_uploaded_image(request):
    uploaded_image = request.session.get('uploaded_image', None)
    return render(request, 'upload.html', {'uploaded_image': uploaded_image})


def about(request):
   
    return render(request, 'about.html') 

# def contact(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')

#         new_contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
#         new_contact.save()

#         return HttpResponse("<h3>Your message has been sent successfully. We will get back to you soon.</h3>")
   
#     return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        
        return render(request, 'message_sent.html')  

    return render(request, 'contact.html')

from django.shortcuts import render

# list of items to search
items = [
    
   {"name": "nature", "image": "beach.jpg"},
    {"name": "people", "image": "peoplea.jpg"},
    {"name": "animals", "image": "animala.jpg"},
    {"name": "food", "image": "fruits.jpg"},
    {"name": "flowers", "image": "flower.jpg"},
    {"name": "books", "image": "books1.jpg"},
    {"name": "architecture", "image": "architecture.jpg"},
    {"name": "digital art", "image": "digiart.jpg"},
    {"name": "fighter jets", "image": "img2.jpg"},
    {"name": "others", "image": "others.jpg"},


    ]

def search(request):
    query = request.GET.get('query', '')  # Get the search query from the URL
    results = []

    if query:
        # Filter items based on the search query (case-insensitive)
        results = [item for item in items if query.lower() in item["name"].lower()]

    return render(request, 'search_results.html', {'query': query, 'results': results})