from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.Employee_view,name='back'),
    path('display/',views.get_all_records,name='display')
]
