from django.shortcuts import render
from django.views.generic import ListView
from todoapp.models import Task
class TaskList(ListView):
    model=Task
