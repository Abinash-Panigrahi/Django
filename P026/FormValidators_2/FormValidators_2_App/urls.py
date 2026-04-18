from django.urls import path
from . import views

urlpatterns = [
    path('validate/',views.Student_view)
]
