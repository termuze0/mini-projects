import json
from datetime import datetime

# File to save tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "completed": False
    })
    print("Task added successfully!")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Created At: {task['created_at']}")
        print("-" * 50)

# Mark a task as completed
def complete_task(tasks):
    list_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete