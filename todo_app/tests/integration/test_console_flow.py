import unittest
from src.models.task import Task
from src.services.todo_manager import TodoManager
from src.cli.console_app import ConsoleApp
import io
import sys
from unittest.mock import patch


class TestConsoleFlow(unittest.TestCase):
    """Integration tests for adding and viewing tasks, and status changes"""

    def test_adding_and_viewing_tasks_integration(self):
        """Integration test for adding and viewing tasks"""
        manager = TodoManager()

        # Add a task
        task = manager.add_task("Test task", "Test description")

        # Verify task was added
        tasks = manager.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test task")
        self.assertEqual(tasks[0].description, "Test description")
        self.assertEqual(tasks[0].status, "Incomplete")

    def test_status_changes_integration(self):
        """Integration test for status changes"""
        manager = TodoManager()

        # Add a task
        task = manager.add_task("Test task")

        # Verify initial status
        self.assertEqual(task.status, "Incomplete")

        # Toggle status
        new_status = manager.toggle_task_status(task.id)
        self.assertEqual(new_status, "Complete")
        self.assertEqual(task.status, "Complete")

        # Toggle back to incomplete
        new_status = manager.toggle_task_status(task.id)
        self.assertEqual(new_status, "Incomplete")
        self.assertEqual(task.status, "Incomplete")

    def test_updating_tasks_integration(self):
        """Integration test for updating tasks"""
        manager = TodoManager()

        # Add a task
        original_task = manager.add_task("Original Title", "Original Description")

        # Update the task
        updated_task = manager.update_task(original_task.id, "New Title", "New Description")

        # Verify the task was updated
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_deleting_tasks_integration(self):
        """Integration test for deleting tasks"""
        manager = TodoManager()

        # Add a task
        task = manager.add_task("Test task", "Test description")

        # Verify task was added
        tasks = manager.get_all_tasks()
        self.assertEqual(len(tasks), 1)

        # Delete the task
        success = manager.delete_task(task.id)

        # Verify task was deleted
        self.assertTrue(success)
        tasks_after_delete = manager.get_all_tasks()
        self.assertEqual(len(tasks_after_delete), 0)


class TestTaskStatus(unittest.TestCase):
    """Unit tests for toggling task status"""

    def test_toggle_task_status_from_incomplete_to_complete(self):
        """Test that a task status can be toggled from incomplete to complete"""
        task = Task("Test task")

        self.assertEqual(task.status, "Incomplete")
        new_status = task.toggle_status()
        self.assertEqual(new_status, "Complete")
        self.assertEqual(task.status, "Complete")

    def test_toggle_task_status_from_complete_to_incomplete(self):
        """Test that a task status can be toggled from complete to incomplete"""
        task = Task("Test task")

        # First toggle to complete
        task.toggle_status()
        self.assertEqual(task.status, "Complete")

        # Then toggle back to incomplete
        new_status = task.toggle_status()
        self.assertEqual(new_status, "Incomplete")
        self.assertEqual(task.status, "Incomplete")


if __name__ == '__main__':
    unittest.main()