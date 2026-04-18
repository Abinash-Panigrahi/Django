from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('cart/',views.cart_view,name='cart'),
    path('all_records/',views.all_records_view,name='all_records')
]