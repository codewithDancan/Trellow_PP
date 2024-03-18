from django.urls import path
from api.views import project_list, project_detail, task_list, task_detail

urlpatterns = [
    path('project', project_list, name='project-list'),
    path('project/<int:id>/', project_detail, name='project-detail'),
    path('task', task_list, name='task-list'),
    path('task/<int:id>/', task_list, name='task-list'),
]
