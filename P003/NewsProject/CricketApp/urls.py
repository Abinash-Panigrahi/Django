from django.urls import path
from . import views

urlpatterns = [
     path('cricket/',views.Cricket_view),
     path('god_of_cricket/',views.God_of_crciket)
]
