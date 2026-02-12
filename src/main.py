import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return [Task(t['id'], t['title'], t['completed']) for t in data]

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([t.to_dict() for t in self.tasks], file, indent=4)

    def add_task(self, title):
        new_id = self.tasks[-1].id + 1 if self.tasks else 1
        self.tasks.append(Task(new_id, title))
        self.save_tasks()

    def view_tasks(self):
        for t in self.tasks:
            status = "✔" if t.completed else "✘"
            print(f"ID: {t.id} | Title: {t.title} | Completed: {status}")

    def update_task(self, task_id, new_title=None, toggle_done=False):
        for t in self.tasks:
            if t.id == task_id:
                if new_title: t.title = new_title
                if toggle_done: t.completed = not t.completed
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()

def main():
    manager = TodoManager()
    while True:
        print("\n--- TODO APP ---")
        print("1. Add | 2. View | 3. Update | 4. Delete | 5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            tid = int(input("Enter ID: "))
            opt = input("Change Title (t) or Toggle Done (d)? ")
            if opt == 't': manager.update_task(tid, new_title=input("New title: "))
            else: manager.update_task(tid, toggle_done=True)
        elif choice == "4":
            manager.delete_task(int(input("Enter ID: ")))
        elif choice == "5":
            break

if __name__ == "__main__":
    main()