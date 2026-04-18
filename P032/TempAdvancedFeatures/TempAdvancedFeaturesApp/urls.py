from django.urls import path
from . import views

urlpatterns = [
    path('india/',views.India_views,name='india'),
    path('usa/',views.USA_views,name='usa'),
    path('uk/',views.UK_views,name='uk')
]