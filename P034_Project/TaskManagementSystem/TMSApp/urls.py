from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('add_task/',views.add_task_view,name='add_task'),
    path('done_task/<int:id>',views.done_task_view,name='done'),
    path('delete_task/<int:id>',views.delete_task_view,name='delete'),
    path('undo_task/<int:id>',views.undo_task_view,name='undo'),
    path('delete_all_incomplete_task/',views.delete_all_incomplete_task,name='delete_all_incomplete_task'),
    path('clear_all_complete_task/',views.clear_all_complete_task,name='clear_all_complete_task'),
    # path('clear_all_complete_task/',views.undo_all_complete_task,name='undo_all_complete_task'),
    path('clear_total_records/',views.clear_total_records_view,name='clear_total_records'),
    path('update/<int:id>',views.update_task_view,name='update'),
]
