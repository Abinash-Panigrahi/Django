from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about_view,name='about'),
    path('home/',views.home_view,name='home'),
    path('contact/',views.contact_view,name='contact'),
]
