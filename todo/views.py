
from django.shortcuts import render
from todos.models import Task
from rest_framework import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

@api_view(['GET'])
def todo_api_list(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)



def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    print(completed_tasks)
    context = {
        'tasks': tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'index.html', context)

