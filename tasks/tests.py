from django.test import TestCase

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
