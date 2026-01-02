# Todo Application

A simple command-line todo application built with Python that stores tasks in memory.

## Features

- Add new tasks with title and optional description
- View all tasks with their details
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone or download the repository
2. Navigate to the `todo_app` directory
3. No additional dependencies needed - uses only Python standard library

## Usage

Run the application with:

```bash
python main.py
```

The application will present a menu with the following options:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Status
6. Exit

## Architecture

The application follows a layered architecture:

- **Models**: Task model representing a single todo item
- **Services**: TodoManager handling business logic and task operations
- **CLI**: Console interface for user interaction

## Testing

Run the unit tests with:

```bash
python -m unittest discover tests/unit
```

Run the integration tests with:

```bash
python -m unittest discover tests/integration
```

## Design Principles

- Simplicity First: Code is written to be easily understood
- Single Responsibility: Each class has one clear purpose
- Explicit Over Implicit: All flows are traceable and clear
- Testable by Design: Code structured for easy testing