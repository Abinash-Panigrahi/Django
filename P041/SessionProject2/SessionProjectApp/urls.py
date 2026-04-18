from django.urls import path
from . import views

urlpatterns = [
    path('session/',views.Session_view),
    path('get_session/',views.get_session,name='get'),
    path('delete_session/',views.delete_session,name='delete'),
    path('page_count/',views.page_count,name='count'),

]
