from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.create_resume_part1, name='resume_part1'),
    path('part2/', views.create_resume_part2, name='resume_part2'),
    path('done/<int:resume_id>/', views.resume_done, name='resume_done'),
]
