from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.WelcomePage_view,name='back'),
    path('signup/',views.SignUp_view,name='signup'),
    path('signin/',views.SignIn_view,name='signin'),

]
