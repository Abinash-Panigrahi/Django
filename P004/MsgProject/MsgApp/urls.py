from django.urls import path,include
from . import views

urlpatterns = [
    path('msg/',views.Wish_view),
]