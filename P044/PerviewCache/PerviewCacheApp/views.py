from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.

def home_view(request):
    return render(request,'PerviewCacheApp/home.html')

@cache_page(60)
def contact_view(request):
    return render(request,'PerviewCacheApp/contact.html')

def about_view(request):
    return render(request,'PerviewCacheApp/about.html')