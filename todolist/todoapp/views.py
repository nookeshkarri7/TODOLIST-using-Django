from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from todoapp.models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
class UserLoginView(LoginView):
    template_name='todoapp/login.html'
    fields="__all__"
    
class UserRegister(FormView):
    template_name='todoapp/register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy("tasks")
    
    
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(UserRegister,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegister,self).get(*args,**kwargs)
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['task_list']=context['task_list'].filter(user=self.request.user)
        context['count_of_tasks']=context['task_list'].filter(complete=False).count()
        searchinput=self.request.GET.get('searchinput') or ""
        if searchinput:
            context['task_list']=context['task_list'].filter(title__icontains=searchinput)        
        context['searchinput']=searchinput
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