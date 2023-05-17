from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from tasks.models import TaskList, Task
from tasks.forms import TaskListForm, TaskForm


@login_required
def home(request):
    task_lists = TaskList.objects.filter(user=request.user)
    incomplete_count = Task.objects.filter(
        task_list__user=request.user, is_completed=False
    ).count()
    completed_count = Task.objects.filter(
        task_list__user=request.user, is_completed=True
    ).count()
    overdue_count = Task.objects.filter(
        task_list__user=request.user, is_completed=False, due_date__lt=timezone.now()
    ).count()
    tasks = Task.objects.filter(due_date__date=timezone.now().date())

    return render(
        request,
        "home.html",
        {
            "task_lists": task_lists,
            "incomplete_count": incomplete_count,
            "completed_count": completed_count,
            "overdue_count": overdue_count,
            "tasks": tasks,
        },
    )


@login_required
def prioritized_tasks(request):
    task_lists = TaskList.objects.filter(user=request.user)
    tasks = Task.objects.filter(
        task_list__user=request.user, is_important=True, is_completed=False
    )

    return render(
        request, "prioritized_tasks.html", {"task_lists": task_lists, "tasks": tasks}
    )


@login_required
def task_list_detail(request, pk):
    task_lists = TaskList.objects.filter(user=request.user)
    task_list_current = get_object_or_404(
        TaskList.objects.filter(user=request.user), pk=pk
    )
    tasks = Task.objects.filter(task_list=task_list_current).order_by('created_at')

    return render(
        request,
        "task_list_detail.html",
        {
            "task_lists": task_lists,
            "task_list_current": task_list_current,
            "tasks": tasks,
        },
    )


@login_required
def create_task_list(request):
    task_lists = TaskList.objects.filter(user=request.user)
    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            return redirect("task_list_detail", pk=task_list.pk)
    else:
        form = TaskListForm()
    return render(
        request, "create_task_list.html", {"form": form, "task_lists": task_lists}
    )


@login_required
def update_task_list(request, pk):
    task_lists = TaskList.objects.filter(user=request.user)
    task_list = get_object_or_404(TaskList.objects.filter(user=request.user), pk=pk)
    if request.method == "POST":
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
            return redirect("task_list_detail", pk=task_list.pk)
    else:
        form = TaskListForm(instance=task_list)
    return render(
        request, "update_task_list.html", {"form": form, "task_lists": task_lists}
    )


@login_required
def delete_task_list(request, pk):
    task_list = get_object_or_404(TaskList.objects.filter(user=request.user), pk=pk)
    task_list.delete()
    return redirect("home")


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task.objects.filter(task_list__user=request.user), pk=pk)
    task_list_pk = task.task_list.pk
    task.delete()
    return redirect("task_list_detail", pk=task_list_pk)


@login_required
def create_task(request, task_list_pk):
    task_list = get_object_or_404(
        TaskList.objects.filter(user=request.user), pk=task_list_pk
    )
    task_lists = TaskList.objects.filter(user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_list = task_list
            task.save()
            return redirect("task_list_detail", pk=task_list_pk)
    else:
        form = TaskForm()
    return render(
        request,
        "create_task.html",
        {"form": form, "task_list": task_list, "task_lists": task_lists},
    )


@login_required
def update_task(request, task_list_pk, task_pk):
    task_list = get_object_or_404(
        TaskList.objects.filter(user=request.user), pk=task_list_pk
    )
    task_lists = TaskList.objects.filter(user=request.user)
    task = get_object_or_404(Task, pk=task_pk, task_list=task_list)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list_detail", pk=task_list_pk)
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        "update_task.html",
        {"form": form, "task_list": task_list, "task": task, "task_lists": task_lists},
    )


@login_required
def toggle_task(request, pk):
    task = get_object_or_404(Task.objects.filter(task_list__user=request.user), pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_list_detail", pk=task.task_list.pk)
