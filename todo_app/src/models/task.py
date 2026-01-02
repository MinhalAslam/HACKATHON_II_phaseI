"""
Task model representing a single todo item in the application.
"""
import uuid
from datetime import datetime
from typing import Optional


class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id (str): Unique identifier for the task, auto-generated
        title (str): Required title of the task, non-empty
        description (str): Optional description of the task, can be empty
        status (str): Task completion status, either "Complete" or "Incomplete"
        created_at (datetime): Timestamp when task was created
    """

    def __init__(self, title: str, description: Optional[str] = None):
        """
        Initialize a new Task instance.

        Args:
            title (str): Required title of the task, non-empty
            description (str, optional): Optional description of the task

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Title must be provided and cannot be empty")

        self.id = str(uuid.uuid4())
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.status = "Incomplete"
        self.created_at = datetime.now()

    def toggle_status(self) -> str:
        """
        Toggle the task status between Complete and Incomplete.

        Returns:
            str: The new status after toggling
        """
        if self.status == "Complete":
            self.status = "Incomplete"
        else:
            self.status = "Complete"
        return self.status

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string representation of the task
        """
        desc = f" - {self.description}" if self.description else ""
        return f"[{self.id[:8]}] {self.title}{desc} [{self.status}]"

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }