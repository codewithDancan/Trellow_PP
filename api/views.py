from rest_framework.response import Response
from api.serializers import ProjectSerializer, TaskSerializer
from project.models import Project
from task.models import Task
from rest_framework.decorators import api_view

@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def project_detail(request,id):
    projects = Project.objects.get(pk=id)
    serializer = ProjectSerializer(projects)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def task_detail(request, id):
    tasks = Task.objects.get(pk=id)
    serializer = TaskSerializer(tasks)
    return Response(serializer.data, status=200)