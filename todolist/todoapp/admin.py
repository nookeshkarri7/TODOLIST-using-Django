from django.contrib import admin
from todoapp.models import Task

#class TaskAdmin(admin.ModelAdmin):
    #@list_display=['']
admin.site.register(Task)