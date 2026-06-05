from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title="Learn CI/CD",
            description="Practice Django pipeline",
            is_done=False,
        )
        self.assertEqual(task.title, "Learn CI/CD")
        self.assertFalse(task.is_done)



class HealthEndpointTest(TestCase):
    def test_health_endpoint_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

