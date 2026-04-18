from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request,'P1App/about.html')

def home_view(request):
    return render(request,'P1App/home.html')

def contact_view(request):
    return render(request,'P1App/contact.html')