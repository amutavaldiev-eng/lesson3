from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('tasks/', get_tasks, name='show_task'),
    path('add/', add_task, name='add_task'),
    path('task/<int:id>/', get_task_id, name='task_detail'),
    path('update/<int:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]