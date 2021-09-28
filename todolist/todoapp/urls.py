from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path("",views.TaskList.as_view(),name='tasks'),
    path("create",views.CreateTask.as_view()),
    path("login",views.UserLoginView.as_view(),name='login'),
    path("logout",views.LogoutView.as_view(next_page='login')),
    path("task/<int:pk>/",views.TaskDetail.as_view()),
    path("update/<int:pk>/",views.TaskUpdate.as_view()),
    path("delete/<int:pk>/",views.TaskDelet.as_view())
]