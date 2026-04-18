from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view),
    path('name/',views.name_view)
]
