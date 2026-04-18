from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.Employee_view,name='back')
]
