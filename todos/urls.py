from django.urls import path
from . import views
from .views import TaskList, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView




urlpatterns = [
    # Login Page
    path('login/', CustomLoginView.as_view(), name='login'),
    # Logout Page
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Register Page
    path('register/', RegisterPage.as_view(), name='register'),
    # Home Page
    path('', TaskList.as_view(), name='tasks'),
    # Add Task
    path('addTask/', views.addTask, name='addTask'),
    # Mark as Done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as UnDone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit Task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete Task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    # API List
    path('api/tasks/', views.todo_api_list, name='todo_api_list'),
 
]
