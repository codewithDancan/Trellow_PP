from django.urls import path
# from api.views import project_list, project_detail, task_list, task_detail
from api.views import ProjectListView, ProjectDetailView, TaskListView, TaskDetailView

urlpatterns = [
    path('project', ProjectListView.as_view(), name='project-list'),
    path('project/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('task', TaskListView.as_view(), name='task-list'),
    path('task/<int:id>/', TaskDetailView.as_view(), name='task-list'),
]
