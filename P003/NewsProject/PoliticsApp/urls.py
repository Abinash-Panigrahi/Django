from django.urls import path
from . import views

urlpatterns = [
     path('about_politics/',views.Politics_view),
     path('cm_of_odisha/',views.CM),
     path('pm_of_india/',views.PM)

]
