from django.http import JsonResponse

from .models import Task


def task_list(request):
    data = list(
        Task.objects.values("id", "title", "description", "is_done", "created_at")
    )
    return JsonResponse(data, safe=False)
