class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = False  # False означает, что задача не выполнена

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"{self.description} (Due: {self.due_date}) - {'Done' if self.status else 'Not Done'}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
        else:
            print("Task not found.")

    def show_current_tasks(self):
        for task in [t for t in self.tasks if not t.status]:
            print(task)

# Создание менеджера задач
task_manager = TaskManager()

# Добавление задач
task_manager.add_task("Изучить Python", "2024-05-01")
task_manager.add_task("Записаться на курс по ИИ", "2024-06-15")

# Показать текущие задачи
print("Текущие задачи:")
task_manager.show_current_tasks()

# Отметить первую задачу как выполненную
task_manager.mark_task_done(0)

# Показать текущие задачи после отметки первой задачи как выполненной
print("\nТекущие задачи после выполнения одной из них:")
task_manager.show_current_tasks()
