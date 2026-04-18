from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home_view,name='home'),
    path('service/',views.Service_view,name='service'),
    path('about/',views.About_view,name='about'),
    path('project/',views.Project_view,name='project'),
    path('testimonial/',views.Testimonial_view,name='testimonial'),
    path('contact/',views.Contact_view,name='contact'),
    path('sign_up/',views.Sign_up_view,name='sign_up'),
    # path('signup_success/',views.Signup_Success_View,name='signup_success'),
    path('sign_in/',views.Sign_in_view,name='sign_in'),
    # path('signin_success/',views.Signin_success_view,name='signin_success'),
    path('dashboard/',views.Dashboard_view,name='dashboard'),
    path('logout/',views.Logout_view,name='logout'),
    path('base/',views.base_view)
    
]
