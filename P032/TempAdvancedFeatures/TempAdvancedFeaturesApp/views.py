from django.shortcuts import render

# Create your views here.

def India_views(request):
    return render(request,'TempAdvancedFeaturesApp/india.html')


def USA_views(request):
    return render(request,'TempAdvancedFeaturesApp/usa.html')


def UK_views(request):
    return render(request,'TempAdvancedFeaturesApp/uk.html')