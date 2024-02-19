class Task:
    def __init__(self, content, deadline, status="not done"):
        self.content = content
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        self.status = "complete"


class TodoList:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def remove_task(self, task):
        self.task_list.remove(task)

    def mark_task_as_done(self, task):
        task.mark_as_done()

    def get_all_tasks(self):
        return self.task_list


task1 = Task("Zadanie 1", "2024-02-20")

todo_list = TodoList()

todo_list.add_task(task1)

todo_list.mark_task_as_done(task1)

all_tasks = todo_list.get_all_tasks()

for task in all_tasks:
    print(f"Zadanie: {task.content}, Deadline: {task.deadline}, Status: {task.status}")

todo_list.remove_task(task1)