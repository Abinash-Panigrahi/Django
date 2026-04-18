from django.shortcuts import render

# Create your views here.

def India_views(request):
    return render(request,'WithoutTemplateInheritanceApp/india.html')


def USA_views(request):
    return render(request,'WithoutTemplateInheritanceApp/usa.html')


def UK_views(request):
    return render(request,'WithoutTemplateInheritanceApp/uk.html')