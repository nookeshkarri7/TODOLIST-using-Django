from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from todoapp.models import Task
class TaskList(ListView):
    model=Task

class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
