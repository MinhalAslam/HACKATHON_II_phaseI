import unittest
from src.models.task import Task


class TestTask(unittest.TestCase):
    """Unit tests for Task creation with required title and optional description"""

    def test_task_creation_with_required_title(self):
        """Test that a task can be created with a required title"""
        task = Task(title="Test task")

        self.assertEqual(task.title, "Test task")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.status, "Incomplete")
        self.assertIsNone(task.description)

    def test_task_creation_with_optional_description(self):
        """Test that a task can be created with title and optional description"""
        task = Task(title="Test task", description="Test description")

        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.status, "Incomplete")


if __name__ == '__main__':
    unittest.main()