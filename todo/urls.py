"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from todos.views import CustomLoginView, RegisterPage, TaskList
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    # Login Page
    path('login/', CustomLoginView.as_view(), name='login'),
    # Logout Page
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Register Page
    path('register/', RegisterPage.as_view(), name='register'),
    # Home Page
    path('', TaskList.as_view(), name='tasks'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    #To Do
    path('todos/', include('todos.urls')),
]
