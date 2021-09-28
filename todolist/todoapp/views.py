from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from todoapp.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
class UserLoginView(LoginView):
    template_name='todoapp/login.html'
    fields="__all__"
    


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['task_list']=context['task_list'].filter(user=self.request.user)
        return context
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name='task'


class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    fields=('title','description','complete')
    success_url=reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CreateTask,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=('title','description','complete')
    success_url=reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskUpdate,self).form_valid(form)


class TaskDelet(LoginRequiredMixin,DeleteView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy("tasks")