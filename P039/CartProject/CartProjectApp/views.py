from django.shortcuts import render,redirect
from .forms import ProductForm

# Create your views here.

def home_view(request):
    if request.method == 'POST':
        form = ProductForm()
        if form.is_valid():
            product = form.cleaned_data['product_Name']
            quantity = form.cleaned_data['quantity']
            response = redirect('home')
            response.set_cookie('product',product)
            response.set_cookie('quantity',quantity)
            return response
    else:
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request,'CartProjectApp/home.html',context)


# def cart_view(request):
#     records = request.COOKIES
#     context = {
#         'record' : records
#     }
#     return render(request,'CartProjectApp/cart.html',context)


def cart_view(request):
    return render(request,'CartProjectApp/cart.html')



def all_records_view(request):
    records = request.COOKIES
    context = {
        'record' : records
    }
    return render(request,'CartProjectApp/allrecords.html',context)