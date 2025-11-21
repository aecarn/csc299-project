# Simple Task Manager (tasks1)

This is a command-line task manager that stores tasks in a JSON file.

## Features
- Add tasks with a title and optional description
- List all saved tasks
- Search tasks by keyword
- Data saved in `tasks.json`

## Requirements
- Python 3.x (no extra packages required)

## How to Run
Open a terminal in the project folder and run:

```bash
python3 tasks1/main.py add "Buy milk" -d "2% at Walgreens"
python3 tasks1/main.py list
python3 tasks1/main.py search milk
