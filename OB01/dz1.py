class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline, "status": "не выполнено"})

    def complete_tasks(self, description):
        found = False
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f"Задача '{description}' выполнена")
                found = True
                break
        if not found:
            print(f"Задача '{description}' не найдена")

    def show_tasks(self):
        print("Задачи:")
        for task in self.tasks:
            if task["status"] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")


o = Task()
o.add_task("сделать заявку", "01.12.2023")
o.add_task("проверить заявку", "03.12.2024")
o.add_task("оплатить заявку", "04.12.2024")
o.add_task("проверить приход по заявке", "07.12.2024")

o.show_tasks()

o.complete_tasks("сделать заявку")
o.complete_tasks("проверить заявку")
