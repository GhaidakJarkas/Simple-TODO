from logging import PlaceHolder
from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new Task'}))
    class Meta:
        model = Task 
        fields = '__all__'
