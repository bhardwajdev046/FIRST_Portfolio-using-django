from django.shortcuts import render,HttpResponse
from home.models import Contact

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contacts=Contact(name=name,email=email,phone=phone,description=description)
        contacts.save()
        print("The data has been written to the database")
    return render(request, 'contacts.html')

# Create your views here.
