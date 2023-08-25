from django import forms
from tasks.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
