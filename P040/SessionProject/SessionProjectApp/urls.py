from django.urls import path
from . import views

urlpatterns = [
    path('session/',views.Session_view),
]
