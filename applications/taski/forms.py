from django.forms import ModelForm
from applications.taski.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'important']