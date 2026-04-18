from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def StudentsForm(request):
    form=StudentForm()
    d={'form':form}
    return render(request,'FormsApp/form.html',d)