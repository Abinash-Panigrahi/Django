from django.urls import path
from . import views

urlpatterns = [
    path('msg/<str:name>',views.msg_view),
    path('add/<int:a>/<int:b>',views.add_view),


]
