from django.shortcuts import render,HttpResponse
from .forms import Employee_Form
from .models import Employee_Model

# Create your views here.

def Employee_view(request):
    if request.method=='POST':
        form=Employee_Form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            desg=form.cleaned_data['desg']
            age=form.cleaned_data['age']
            sal=form.cleaned_data['sal']
            address=form.cleaned_data['address']
            model=Employee_Model(name=name,desg=desg,age=age,sal=sal,address=address)
            model.save()
            context={
                'name':name
            }
            return render(request,'EmployeeInfoApp/success.html',context)

    else:
        form=Employee_Form(request.POST)
        context={
            'form':form
        }
        return render(request,'EmployeeInfoApp/forms.html',context)
    


def get_all_records(request):
    all_records=Employee_Model.objects.all()
    context={
        'all_records':all_records
    }
    return render(request,'EmployeeInfoApp/display.html',context)



# def delete_records(request,id):
#     delete_records=Employee_Model.objects.get(id=id)
#     delete_records.delete()
#     return render(request,'EmployeeInfoApp/delete.html')

    #  <a href="{% url 'delete' id=46 %}">Delete record</a>         /In success.html

   
