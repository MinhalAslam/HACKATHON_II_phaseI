# Data Model: Phase I Todo App

## Entity: Task

**Description**: Represents a single todo item in the application

**Fields**:
- `id` (integer): Unique identifier for the task, auto-generated
- `title` (string): Required title of the task, non-empty
- `description` (string): Optional description of the task, can be empty
- `status` (string): Task completion status, either "Complete" or "Incomplete"

**Validation Rules**:
- `title` must not be empty or null when creating a task
- `id` must be unique within the application
- `status` must be one of the allowed values: "Complete" or "Incomplete"

**State Transitions**:
- From "Incomplete" to "Complete" when marked as done
- From "Complete" to "Incomplete" when marked as not done

## Entity: TodoManager

**Description**: Manages the collection of tasks and provides business logic operations

**Attributes**:
- `tasks` (dictionary): Collection of tasks indexed by ID
- `next_id` (integer): Counter for generating next unique task ID

**Operations**:
- Add task: Creates a new task with auto-generated ID and "Incomplete" status
- Get all tasks: Returns the complete collection of tasks
- Update task: Modifies existing task title or description
- Delete task: Removes a task by ID
- Toggle status: Changes task status between Complete/Incomplete
- Validate task existence: Checks if a task exists before operations