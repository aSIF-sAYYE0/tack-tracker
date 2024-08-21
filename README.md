# Task Tracker CLI

This is a simple command-line interface (CLI) application for tracking tasks.

## Features
- Add, update, and delete tasks
- Mark tasks as in-progress or done
- List tasks by status

## Usage

```bash
# Adding a new task
python task_cli.py add "Buy groceries"

# Updating a task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Deleting a task
python task_cli.py delete 1

# Marking a task as in-progress
python task_cli.py mark-in-progress 1

# Marking a task as done
python task_cli.py mark-done 1

# Listing all tasks
python task_cli.py list

# Listing tasks by status
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress

https://roadmap.sh/projects/task-tracker
