from django.shortcuts import render

from django.http import HttpResponse
from . models import Task
from django.shortcuts import redirect

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

