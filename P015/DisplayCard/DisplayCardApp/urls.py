from django.urls import path
from . import views

urlpatterns = [
    path('get_records/',views.retrieve_view,name='all_records'),
    path('get_specific_record/<int:id>',views.get_specific_record,name='specific_card')
]
