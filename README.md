# Mini Project: OOP-Based Todo App (Local JSON Storage)

This is a simple Command Line Interface (CLI) Todo application implemented with
Object-Oriented Programming and local JSON persistence.

Features

- Add, list, update, mark complete/uncomplete, delete todos
- Tasks are saved to `todos.json` and reloaded when the app starts

How to run

1. (Optional) create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Run the app:

```bash
python todo.py
```

Type `help` for available commands inside the app.

Persistence & serialization

Tasks are instances of the `Task` class. When saved, each task is converted to a
dictionary via `Task.to_dict()` and written to `todos.json` with `json.dump`.
When the app starts it reads `todos.json`, parses the JSON, and converts each
dict back to a `Task` object via `Task.from_dict()`.

.gitignore

The repo includes a `.gitignore` that excludes virtual environments and cache.

License

MIT
