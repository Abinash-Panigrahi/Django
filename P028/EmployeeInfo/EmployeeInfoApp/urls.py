from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.Employee_view,name='back'),
    path('get_records/',views.get_all_records,name='display'),
    # path('delete/<int:id>/',views.delete_records,name='delete')
]
