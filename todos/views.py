from django.shortcuts import render

from django.http import HttpResponse
from . models import Task
from django.shortcuts import redirect, get_object_or_404

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    
    else:
        context = {
            'get_task': get_task,
        }    
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer



@api_view(['GET'])
def todo_api_list(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


 
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context
    