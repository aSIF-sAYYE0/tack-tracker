import json
import sys
from datetime import datetime
import os

# Correct path to the tasks.json file
TASKS_FILE = 'data/tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {new_task["id"]})')

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully')
            return
    print(f'Task {task_id} not found')

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully')

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}')
            return
    print(f'Task {task_id} not found')

def list_tasks(status=None):
    tasks = load_tasks()
    for task in tasks:
        if status and task['status'] != status:
            continue
        print(f'{task["id"]}: {task["description"]} [{task["status"]}]')

if __name__ == "__main__":
    command = sys.argv[1]
    if command == 'add':
        add_task(' '.join(sys.argv[2:]))
    elif command == 'update':
        update_task(int(sys.argv[2]), ' '.join(sys.argv[3:]))
    elif command == 'delete':
        delete_task(int(sys.argv[2]))
    elif command == 'mark-in-progress':
        mark_task(int(sys.argv[2]), 'in-progress')
    elif command == 'mark-done':
        mark_task(int(sys.argv[2]), 'done')
    elif command == 'list':
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print(f'Unknown command: {command}')
