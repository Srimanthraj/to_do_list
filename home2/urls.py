from django.urls import path, include
from . import views


urlpatterns = [
    path("post2/", views.homepage, name="home"),
    path("tasks2/update/<int:id>/", views.UpdateTask, name="update"),
    path("tasks2/", views.taskspage, name="tasks"),
    path("tasks2/deleteTask/<int:id>/", views.deleteTask, name="deleteTasks"),


]
