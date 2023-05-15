from django.contrib import admin

from tasks.models import TaskList, Task


class TaskAdmin(admin.ModelAdmin):
    pass


class TaskListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
