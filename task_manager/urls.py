"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from tasks import views as tasks_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', tasks_views.home, name='home'),
    path('tasks/prioritized/', tasks_views.prioritized_tasks, name='prioritized_tasks'),
    path('task-list/<int:pk>/', tasks_views.task_list_detail, name='task_list_detail'),
    path('task-list/<int:pk>/delete/', tasks_views.delete_task_list, name='delete_task_list'),
    path('task-list/create/', tasks_views.create_task_list, name='create_task_list'),
    path('task-list/<int:pk>/update/', tasks_views.update_task_list, name='update_task_list'),
    path('task-list/<int:task_list_pk>/task/create/', tasks_views.create_task, name='create_task'),
    path('task-list/<int:task_list_pk>/task/<int:task_pk>/update/', tasks_views.update_task, name='update_task'),
    path('task/<int:pk>/toggle/', tasks_views.toggle_task, name='toggle_task'),
    path('task/<int:pk>/delete/', tasks_views.delete_task, name='delete_task'),

    path('register/', accounts_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

handler404 = 'accounts.views.custom_page_not_found_view'
