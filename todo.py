

import json
import os
from typing import List, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


class Task:
    

    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self) -> dict:
        
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(d: dict) -> "Task":
        
        return Task(d["id"], d["title"], d.get("completed", False))


class TodoManager:
    

    def __init__(self, data_file: str = DATA_FILE):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.load()

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add_task(self, title: str) -> Task:
        new_task = Task(self._next_id(), title)
        self.tasks.append(new_task)
        self.save()
        return new_task

    def get_task(self, task_id: int) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def update_task_title(self, task_id: int, new_title: str) -> bool:
        t = self.get_task(task_id)
        if not t:
            return False
        t.title = new_title
        self.save()
        return True

    def set_task_completed(self, task_id: int, completed: bool) -> bool:
        t = self.get_task(task_id)
        if not t:
            return False
        t.completed = completed
        self.save()
        return True

    def delete_task(self, task_id: int) -> bool:
        t = self.get_task(task_id)
        if not t:
            return False
        self.tasks.remove(t)
        self.save()
        return True

    def list_tasks(self) -> List[Task]:
        return list(self.tasks)

    def save(self) -> None:
        """Serialize tasks to the JSON file."""
        data = [t.to_dict() for t in self.tasks]
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self) -> None:
        """Load tasks from the JSON file, converting them to Task objects."""
        if not os.path.exists(self.data_file):
            self.tasks = []
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(d) for d in data]
        except (json.JSONDecodeError, IOError):
            # If file is corrupted or unreadable, start with empty list
            self.tasks = []


def print_help() -> None:
    print()

    


def main():
    mgr = TodoManager()
    print("OOP Todo CLI — type 'help' for commands")
    while True:
        try:
            raw = input("todo> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not raw:
            continue
        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "help":
            print_help()
        elif cmd == "add":
            if not args:
                print("Usage: add <title>")
                continue
            title = " ".join(args)
            t = mgr.add_task(title)
            print(f"Added: [{t.id}] {t.title}")
        elif cmd == "list":
            tasks = mgr.list_tasks()
            if not tasks:
                print("No todos yet.")
                continue
            for t in tasks:
                status = "✔" if t.completed else " "
                print(f"[{t.id}] [{status}] {t.title}")
        elif cmd == "update":
            if len(args) < 2:
                print("Usage: update <id> <new title>")
                continue
            try:
                tid = int(args[0])
            except ValueError:
                print("Invalid id")
                continue
            new_title = " ".join(args[1:])
            if mgr.update_task_title(tid, new_title):
                print("Updated.")
            else:
                print("Task not found.")
        elif cmd in ("complete", "uncomplete"):
            if len(args) != 1:
                print(f"Usage: {cmd} <id>")
                continue
            try:
                tid = int(args[0])
            except ValueError:
                print("Invalid id")
                continue
            completed = cmd == "complete"
            if mgr.set_task_completed(tid, completed):
                print("Updated status.")
            else:
                print("Task not found.")
        elif cmd == "delete":
            if len(args) != 1:
                print("Usage: delete <id>")
                continue
            try:
                tid = int(args[0])
            except ValueError:
                print("Invalid id")
                continue
            if mgr.delete_task(tid):
                print("Deleted.")
            else:
                print("Task not found.")
        elif cmd in ("exit", "quit"):
            break
        else:
            print("Unknown command. Type 'help' for commands.")


if __name__ == "__main__":
    main()



