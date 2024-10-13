from collections import deque

class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()

    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task added: {task}")

    def execute_task(self):
        if self.task_queue:
            task = self.task_queue.popleft()
            print(f"Executing: {task}")
        else:
            print("No tasks to execute.")

    def view_tasks(self):
        if self.task_queue:
            print("Pending Tasks:")
            for i, task in enumerate(self.task_queue, 1):
                print(f"{i}. {task}")
        else:
            print("No pending tasks.")

# Run example
scheduler = TaskScheduler()
scheduler.add_task("Send Email")
scheduler.add_task("Generate Report")
scheduler.execute_task()
scheduler.view_tasks()
