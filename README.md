# Task-Checklist

This is a terminal-based checklist application designed to help users organize their tasks and subjects efficiently.

## Project Structure

The project is organized into three main components:

- `main.py` - The main entry point of the application.
- `subject.py` - Handles the subject-related functionalities.
- `tasks.py` - Manages the tasks within each subject.

## Features

### Main Menu

- **Create Subject**: 
  - Lists existing subjects.
  - Prompts user to input a new subject name.
  - Confirms or cancels the creation of the new subject.

- **Edit Subject**:
  - Lists subjects for selection by index number.
  - Provides options to add or remove tasks within the selected subject.
    - **Add Task**:
      - Lists tasks in the selected subject.
      - Prompts user to input a new task name.
      - Adds the new task to the list and displays the updated task list.
      - Option to return to the main menu.
    - **Remove Task**:
      - Lists tasks in the selected subject.
      - Prompts user to input the task name to be removed.
      - Confirms removal and displays the updated task list.
      - Option to return to the main menu.

- **Remove Subject**:
  - Lists subjects for selection by index number.
  - Confirms removal of the selected subject.
  - Option to cancel and return to the main menu.

- **Check/Uncheck Task**:
  - Lists subjects and their tasks with indices.
  - Allows toggling of checkmarks for tasks.
  - Displays the updated list with checked tasks.
  - Returns to the main menu.

- **Exit**:
  - Exits the program.

## Usage Instructions

Create a Directory in the cloned repo called Data, and create files subjects.txt and tasks.txt to store data to files.

1. **Create a Subject**: Select the "Create Subject" option from the main menu, input the subject name, and confirm.
2. **Edit a Subject**: Choose the "Edit Subject" option, select a subject by its index number, and choose to add or remove tasks.
3. **Remove a Subject**: Pick the "Remove Subject" option, select a subject by its index number, and confirm the removal.
4. **Check/Uncheck a Task**: Opt for "Check/Uncheck Task," select the subject and task by their index numbers, and toggle the checkmark.
5. **Exit**: Select the "Exit" option to close the application.

### Navigation

- Use `--` to go back in the UI.
- Enter the number next to the listed subjects or tasks to edit, check, or remove them.
- Type the name of the task or subject when prompted to add them.

## Requirements

- This application currently only works in Unix environments.

## Acknowledgements

This project is a continuation of previous efforts, incorporating lessons learned to create a more manageable and user-friendly checklist application.
