from django.urls import path
from . import views

urlpatterns = [
    path('check/',views.Password_view,name='back')
]
