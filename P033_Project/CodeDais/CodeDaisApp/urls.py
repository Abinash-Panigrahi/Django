from django.urls import path
from . import views

urlpatterns = [
    path('base/',views.Base_view,name='home'),
    path('front/',views.Front_view,name='front'),
    path('about/',views.About_view,name='about'),
    path('python/',views.Python_view,name='python'),
    path('signup/',views.SignUp_view,name='signup'),
    path('signin/',views.Sign_In_view,name='signin'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),

]
