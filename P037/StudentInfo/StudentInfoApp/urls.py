from django.urls import path
from . import views

urlpatterns = [
    path('education_form/',views.education_form_view),
    path('personal_form/',views.personal_form_view,name='personal_form'),
    path('extra_curicular_form/',views.extra_curicular_form_view,name='extra_curicular_form'),
    path('data_link/',views.data_link,name='data_link'),
    path('all_data/',views.all_data,name='all_data')
]
