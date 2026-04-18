from django.shortcuts import render
from .forms import StudentForms

# Create your views here.

def Student_view(request):
    form=StudentForms()
    d={'form':form}
    return render(request,'FormFieldApp/home.html',d)
