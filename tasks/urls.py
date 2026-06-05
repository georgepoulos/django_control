from django.urls import path

from .views import task_list, health

urlpatterns = [
    path("tasks/", task_list, name="task_list"),
    path("health/", health, name="health"),
]
