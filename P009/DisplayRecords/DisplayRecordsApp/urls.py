from django.urls import path
from . import views

urlpatterns = [
    path('Shirt/',views.retrieve_view),
   
]


