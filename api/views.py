from rest_framework.response import Response
from api.serializers import ProjectSerializer, TaskSerializer
from project.models import Project
from task.models import Task
from rest_framework.decorators import api_view
from rest_framework import generics

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
class TaskListView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

# @api_view(['GET'])
# def project_list(request):
#     projects = Project.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return Response(serializer.data, status=200)

# @api_view(['GET'])
# def project_detail(request,id):
#     projects = Project.objects.get(pk=id)
#     serializer = ProjectSerializer(projects)
#     return Response(serializer.data, status=200)

# @api_view(['GET'])
# def task_list(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data, status=200)

# @api_view(['GET'])
# def task_detail(request, id):
#     tasks = Task.objects.get(pk=id)
#     serializer = TaskSerializer(tasks)
#     return Response(serializer.data, status=200)