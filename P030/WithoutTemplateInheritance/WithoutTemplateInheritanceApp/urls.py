from django.urls import path
from . import views

urlpatterns = [
    path('india/',views.India_views),
    path('usa/',views.USA_views),
    path('uk/',views.UK_views)
]