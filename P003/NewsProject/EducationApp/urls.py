from django.urls import path
from . import views

urlpatterns = [
     path('education/',views.Education_view),
     path('todays_education/',views.Now_a_days_Education_system)
]
