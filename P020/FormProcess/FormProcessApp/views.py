from django.shortcuts import render
from .forms import EmployeeForms

# Create your views here.

def Employee_view(request):
    if request.method=='POST':
        form=EmployeeForms(request.POST)
        d={'form':form}
        return render(request,'FormProcessApp/welcome.html',d)
    else:
        form=EmployeeForms()
        d={'form':form}
        return render(request,'FormProcessApp/forms.html',d)

