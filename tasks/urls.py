from django.urls import path

from .views import health, home, task_list

urlpatterns = [
    path("tasks/", task_list, name="task_list"),
    path("health/", health, name="health"),
    path("home/", home, name="home"),
]
