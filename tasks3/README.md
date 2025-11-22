# Task 3 — Task Manager with Tests (tasks3)

This directory contains a Python package version of the command-line
task manager, built using `uv` and tested with `pytest`.

It extends the earlier prototypes (tasks1 / tasks2) and adds:

- A proper Python package layout under `src/`
- An entrypoint so the app can be run with `uv run tasks3`
- Automated tests using `pytest` (including the `inc` demo and real PKMS logic)

## Features

- Store tasks in a JSON file (`tasks.json`)
- Add tasks with a title and optional description
- List all tasks
- Mark tasks as completed (with a `done` flag)
- Compute the next task ID based on existing tasks
- Basic tests for:
  - `inc(n)` helper function
  - `next_id(tasks)` logic in the task manager

## Requirements

- Python 3.13+ (handled automatically by `uv`)
- `uv` installed globally
- `pytest` as a dev dependency (already configured in this project)

## How to Run the Task Manager

From the `tasks3` directory:

```bash
uv sync           # install dependencies and this package into the .venv
uv run tasks3 -- list
uv run tasks3 -- add "Buy milk" -d "2% at Walgreens"
uv run tasks3 -- list
uv run tasks3 -- done 1
