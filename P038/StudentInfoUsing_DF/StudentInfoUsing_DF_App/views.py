from django.shortcuts import render,redirect
from .forms import EducationForm,PersonalForm,ExtracuricularForm

# Create your views here.

def education_form_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            college = form.cleaned_data['college']
            degree = form.cleaned_data['degree']
            mark = form.cleaned_data['mark']
            response = redirect('personal_form')
            response.set_cookie('college',college)
            response.set_cookie('degree',degree)
            response.set_cookie('mark',mark)
            return response
    else:
        form = EducationForm()
    context = {
        'form' : form
       }
    return render(request,'StudentInfoUsing_DF_App/education_form.html',context)


def personal_view(request): 
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            response = redirect('extra_curicular_form')
            response.set_cookie('name',name)
            response.set_cookie('address',address)
            response.set_cookie('email',email)
            return response
    else:
        form = PersonalForm()
    context = {
        'form' : form
       }
    return render(request,'StudentInfoUsing_DF_App/personal_form.html',context)


def extra_curicular_view(request):

    if request.method == 'POST':
        form = ExtracuricularForm(request.POST)
        if form.is_valid():
            fav_sports = form.cleaned_data['fav_sports']
            fav_actor = form.cleaned_data['fav_actor']
            response = redirect('link')
            response.set_cookie('fav_sports',fav_sports)
            response.set_cookie('fav_actor',fav_actor)
            return response
    else:
        form = ExtracuricularForm()
    context = {
        'form' : form
       }
    return render(request,'StudentInfoUsing_DF_App/extra_curicular.html',context)

def link_view(request):
    return render(request,'StudentInfoUsing_DF_App/link.html')

def all_records_view(request):
    records = request.COOKIES
    context = {
        'records' : records
    }
    return render(request,'StudentInfoUsing_DF_App/all_records.html',context)

