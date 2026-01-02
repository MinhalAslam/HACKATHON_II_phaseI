#!/usr/bin/env python3
"""
Quick validation script to test the main.py file functionality.
"""
from src.models.task import Task
from src.services.todo_manager import TodoManager
from src.cli.console_app import ConsoleApp


def test_basic_functionality():
    """Test the basic functionality of the todo app"""
    print("Testing basic functionality...")

    # Test Task creation
    task = Task("Test task")
    assert task.title == "Test task"
    assert task.status == "Incomplete"
    print("PASS: Task creation works")

    # Test TodoManager
    manager = TodoManager()
    task1 = manager.add_task("First task", "Description 1")
    task2 = manager.add_task("Second task")

    tasks = manager.get_all_tasks()
    assert len(tasks) == 2
    print("PASS: Task management works")

    # Test update
    updated_task = manager.update_task(task1.id, "Updated task")
    assert updated_task.title == "Updated task"
    print("PASS: Task update works")

    # Test status toggle
    original_status = task2.status
    new_status = manager.toggle_task_status(task2.id)
    assert new_status != original_status
    print("PASS: Status toggle works")

    # Test delete
    initial_count = len(manager.get_all_tasks())
    success = manager.delete_task(task1.id)
    assert success
    assert len(manager.get_all_tasks()) == initial_count - 1
    print("PASS: Task deletion works")

    print("\nAll basic functionality tests passed!")


def test_console_app():
    """Test that ConsoleApp can be initialized"""
    print("\nTesting ConsoleApp initialization...")
    app = ConsoleApp()
    assert app.manager is not None
    print("PASS: ConsoleApp initialization works")


if __name__ == "__main__":
    test_basic_functionality()
    test_console_app()
    print("\nSUCCESS: All validation tests passed! The main.py file should work correctly.")