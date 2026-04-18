from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Profile_View,name='back'),
    path('about/<int:id>',views.About_view,name='about')
] 
