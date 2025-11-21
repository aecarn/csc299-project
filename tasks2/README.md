# Simple Task Manager (tasks2)

This is a command-line task manager that stores tasks in a JSON file.  
This version includes updates made for tasks2.

## Features
- Add tasks with a title and optional description  
- List all saved tasks  
- Search tasks by keyword  
- **Mark tasks as completed using the new `done` command**  
- Data saved in `tasks.json`  
- **Completed tasks show a checkmark (✓) when listed**

## New in tasks2
- Tasks now include a `"done"` field  
- Added the `done <id>` command to mark a task as finished  
- Updated list output to display completion status  

## Requirements
- Python 3.x (no extra packages required)

## How to Run
Open a terminal in the project folder and run:

```bash
python3 tasks2/main.py add "Buy milk" -d "2% at Walgreens"
python3 tasks2/main.py list
python3 tasks2/main.py done 1
python3 tasks2/main.py search milk

