from django.shortcuts import redirect, render

from tasks.models import Task


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    tasks = Task.objects.filter(task_list__user=request.user).select_related('task_list')

    return render(request, 'home.html', {"tasks": tasks})
