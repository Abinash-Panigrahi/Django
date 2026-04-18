from django.shortcuts import render
from .forms import EmployeeForms

# Create your views here.

def Employee_view(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        e_mail=request.POST['e_mail']
        d={'name':name,'age':age,'e_mail':e_mail}
        return render(request,'FormProcess_2App/welcome.html',d)
    
    else:
        form=EmployeeForms()
        d={'form':form}
        return render(request,'FormProcess_2App/form.html',d)