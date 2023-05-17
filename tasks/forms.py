from django import forms
from tasks.models import TaskList, Task


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "due_date", "is_important"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["due_date"].widget.attrs["class"] = "form-control"
        self.fields["is_important"].widget.attrs["class"] = "form-check-input"
