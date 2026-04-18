from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.country,name='return'),
    path('specific_record/<int:id>',views.specific_country,name='specific_record')
]
