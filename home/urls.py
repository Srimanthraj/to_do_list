from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homepage, name="home"),
    path('favicon.ico', views.ignore_favicon),
    path("index1/", views.index1, name="home"),
    path("index2/", views.index2, name="home"),
    path("house/", views.house, name="house"),
    path("tasks/update/<int:id>/", views.UpdateTask, name="update"),
    path("tasks/", views.taskspage, name="tasks"),
    path("tasks/deleteTask/<int:id>/", views.deleteTask, name="deleteTasks"),


]
