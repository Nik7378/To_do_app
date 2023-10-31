from django.urls import path
from .import views

urlpatterns = [
    path('task', views.task_form, name="taskform"),
    path('add_task', views.add_task, name="add_task"),
    path('', views.get_list, name="get_list"),
    path('edit/<rid>', views.edit, name="edit"),
    path('delete/<rid>', views.delete, name="delete")
]
