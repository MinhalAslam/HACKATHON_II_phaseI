"""
Console interface for the Todo application.
"""
from typing import Optional
from src.services.todo_manager import TodoManager


class ConsoleApp:
    """
    Console interface layer that handles all user interaction.
    Menu rendering, user input parsing, output formatting.
    Delegates actions to TodoManager.
    """

    def __init__(self):
        """
        Initialize the ConsoleApp with a TodoManager instance.
        """
        self.manager = TodoManager()

    def display_tasks(self, tasks=None):
        """
        Display all tasks in a readable format.

        Args:
            tasks: List of tasks to display. If None, gets all tasks from manager.
        """
        if tasks is None:
            tasks = self.manager.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in tasks:
            print(f"ID: {task.id[:8]}")
            print(f"Title: {task.title}")
            if task.description:
                print(f"Description: {task.description}")
            print(f"Status: {task.status}")
            print("-" * 30)

    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*50)
        print("TODO APPLICATION")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Status")
        print("6. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get user choice from the menu.

        Returns:
            str: User's menu choice
        """
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            return "6"  # Return exit choice

    def add_task_interface(self):
        """
        Interface for adding a new task.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Title is required!")
            return

        description_input = input("Enter task description (optional, press Enter to skip): ").strip()
        description = description_input if description_input else None

        try:
            task = self.manager.add_task(title, description)
            print(f"Task added successfully! ID: {task.id[:8]}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks_interface(self):
        """
        Interface for viewing all tasks.
        """
        print("\n--- View All Tasks ---")
        self.display_tasks()

    def update_task_interface(self):
        """
        Interface for updating a task.
        """
        print("\n--- Update Task ---")
        task_id = input("Enter task ID to update: ").strip()

        if not task_id:
            print("Error: Task ID is required!")
            return

        # Check if task exists
        task = self.manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id[:8]} not found!")
            return

        print(f"Current task: {task.title}")
        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        new_title = new_title if new_title else None

        current_desc = task.description if task.description else ""
        new_description = input(f"Enter new description (current: '{current_desc}', press Enter to keep current): ").strip()
        new_description = new_description if new_description else None

        try:
            updated_task = self.manager.update_task(task_id, new_title, new_description)
            if updated_task:
                print("Task updated successfully!")
            else:
                print("Error updating task.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task_interface(self):
        """
        Interface for deleting a task.
        """
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID to delete: ").strip()

        if not task_id:
            print("Error: Task ID is required!")
            return

        success = self.manager.delete_task(task_id)
        if success:
            print("Task deleted successfully!")
        else:
            print(f"Error: Task with ID {task_id[:8]} not found!")

    def mark_task_status_interface(self):
        """
        Interface for marking task status.
        """
        print("\n--- Mark Task Status ---")
        task_id = input("Enter task ID to toggle status: ").strip()

        if not task_id:
            print("Error: Task ID is required!")
            return

        # Check if task exists
        task = self.manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id[:8]} not found!")
            return

        print(f"Current task: {task.title} - Status: {task.status}")
        new_status = self.manager.toggle_task_status(task_id)
        if new_status:
            print(f"Task status updated to: {new_status}")
        else:
            print("Error updating task status.")

    def run(self):
        """
        Main application loop.
        """
        print("Welcome to the Todo Application!")
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task_interface()
            elif choice == "2":
                self.view_tasks_interface()
            elif choice == "3":
                self.update_task_interface()
            elif choice == "4":
                self.delete_task_interface()
            elif choice == "5":
                self.mark_task_status_interface()
            elif choice == "6":
                print("\nThank you for using the Todo Application!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")

            # Pause to let user see the result
            input("\nPress Enter to continue...")


def main():
    """
    Entry point for the console application.
    """
    app = ConsoleApp()
    app.run()


if __name__ == "__main__":
    main()