from django.urls import path
from . import views

urlpatterns = [
    path('education/',views.education_form_view),
    path('personal_form/',views.personal_view,name='personal_form'),
    path('extra_curicular_form/',views.extra_curicular_view,name='extra_curicular_form'),
    path('link/',views.link_view,name='link'),
    path('allrecords/',views.all_records_view,name='allrecords')
]
