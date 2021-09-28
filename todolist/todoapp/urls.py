from django.urls import path
from . import views
urlpatterns=[
    path("",views.TaskList.as_view(),name='tasks'),
    path("create",views.CreateTask.as_view()),
    path("task/<int:pk>/",views.TaskDetail.as_view()),
    path("update/<int:pk>/",views.TaskUpdate.as_view())
]