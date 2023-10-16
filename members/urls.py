from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.loginpage),
    # path("tasks/update/<int:id>/", views.UpdateTask, name="update"),


]
