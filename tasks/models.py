from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    due_date = models.DateTimeField(null=True, blank=True)
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def is_expired(self):
        return not self.is_completed and self.due_date > timezone.now()
