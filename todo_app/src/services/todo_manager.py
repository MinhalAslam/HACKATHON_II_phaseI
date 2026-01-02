"""
TodoManager service to manage the collection of tasks and provide business logic operations.
"""
from typing import Dict, List, Optional
from src.models.task import Task


class TodoManager:
    """
    Manages the collection of tasks and provides business logic operations.

    Attributes:
        tasks (dict): Collection of tasks indexed by ID
        next_id (int): Counter for generating next unique task ID (not used since we use UUIDs)
    """

    def __init__(self):
        """
        Initialize the TodoManager with an empty task collection.
        """
        self.tasks: Dict[str, Task] = {}

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Creates a new task with auto-generated ID and "Incomplete" status.

        Args:
            title (str): Required title of the task
            description (str, optional): Optional description of the task

        Returns:
            Task: The newly created task

        Raises:
            ValueError: If title is empty or None
        """
        task = Task(title=title, description=description)
        self.tasks[task.id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Returns the complete collection of tasks.

        Returns:
            List[Task]: List of all tasks
        """
        return list(self.tasks.values())

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (str): The ID of the task to retrieve

        Returns:
            Task: The task with the given ID, or None if not found
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, title: Optional[str] = None,
                   description: Optional[str] = None) -> Optional[Task]:
        """
        Modifies existing task title or description.

        Args:
            task_id (str): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        if title is not None:
            if not title.strip():
                raise ValueError("Title must be provided and cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip() if description else None

        return task

    def delete_task(self, task_id: str) -> bool:
        """
        Removes a task by ID.

        Args:
            task_id (str): The ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def toggle_task_status(self, task_id: str) -> Optional[str]:
        """
        Changes task status between Complete/Incomplete.

        Args:
            task_id (str): The ID of the task to toggle

        Returns:
            str: The new status if successful, None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        return task.toggle_status()

    def validate_task_exists(self, task_id: str) -> bool:
        """
        Checks if a task exists before operations.

        Args:
            task_id (str): The ID of the task to check

        Returns:
            bool: True if task exists, False otherwise
        """
        return task_id in self.tasks