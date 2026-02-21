
from django.shortcuts import render
from todos.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    print(completed_tasks)
    context = {
        'tasks': tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'index.html', context)

