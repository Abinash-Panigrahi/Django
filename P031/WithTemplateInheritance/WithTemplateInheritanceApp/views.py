from django.shortcuts import render

# Create your views here.

def India_views(request):
    return render(request,'WithTemplateInheritanceApp/india.html')


def USA_views(request):
    return render(request,'WithTemplateInheritanceApp/usa.html')


def UK_views(request):
    return render(request,'WithTemplateInheritanceApp/uk.html')