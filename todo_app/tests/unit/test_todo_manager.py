import unittest
from src.models.task import Task
from src.services.todo_manager import TodoManager


class TestTodoManager(unittest.TestCase):
    """Unit tests for viewing all tasks functionality"""

    def test_view_all_tasks_empty_list(self):
        """Test that viewing all tasks returns empty list when no tasks exist"""
        manager = TodoManager()
        tasks = manager.get_all_tasks()

        self.assertEqual(len(tasks), 0)
        self.assertIsInstance(tasks, list)

    def test_view_all_tasks_with_tasks(self):
        """Test that viewing all tasks returns all tasks with correct details"""
        manager = TodoManager()

        # Add some tasks
        task1 = manager.add_task("Task 1", "Description 1")
        task2 = manager.add_task("Task 2")

        tasks = manager.get_all_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)

        # Verify task details are preserved
        for task in tasks:
            self.assertIsInstance(task, Task)
            self.assertIsNotNone(task.id)
            self.assertIsNotNone(task.title)
            self.assertIn(task.status, ["Complete", "Incomplete"])

    def test_update_task_details(self):
        """Unit test for updating task details"""
        manager = TodoManager()

        # Add a task
        original_task = manager.add_task("Original Title", "Original Description")

        # Update the task
        updated_task = manager.update_task(original_task.id, "New Title", "New Description")

        # Verify the task was updated
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_update_task_title_only(self):
        """Unit test for updating task title only"""
        manager = TodoManager()

        # Add a task
        original_task = manager.add_task("Original Title", "Original Description")

        # Update only the title
        updated_task = manager.update_task(original_task.id, "New Title")

        # Verify only the title was updated
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "Original Description")

    def test_update_task_description_only(self):
        """Unit test for updating task description only"""
        manager = TodoManager()

        # Add a task
        original_task = manager.add_task("Original Title", "Original Description")

        # Update only the description
        updated_task = manager.update_task(original_task.id, description="New Description")

        # Verify only the description was updated
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Original Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_delete_task(self):
        """Unit test for deleting tasks"""
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

    def test_delete_nonexistent_task(self):
        """Unit test for deleting a non-existent task"""
        manager = TodoManager()

        # Attempt to delete a non-existent task
        success = manager.delete_task("nonexistent-id")

        # Verify the operation failed gracefully
        self.assertFalse(success)


if __name__ == '__main__':
    unittest.main()