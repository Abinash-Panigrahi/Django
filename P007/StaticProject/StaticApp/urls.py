from django.urls import path
from . import views

urlpatterns = [
    path('avenger/',views.avenger_view)
]