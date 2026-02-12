This is a command-line Todo application written in Python.
The application allows users to add, view, update, and delete tasks.
All tasks are stored persistently in a JSON file.

# Mini Project: OOP-Based Todo App (Local JSON Storage)

This is a small Command Line Interface (CLI) Todo app built with an object-oriented design and local JSON persistence.

Contents

- Source: `src/main.py`
- Local data file: `src/todos.json` (app reads/writes here)

Features

- Add Todo (title)
- View Todos (ID, title, completed)
- Update Todo (edit title, toggle completed)
- Delete Todo (by ID)
- Persistent storage via JSON: tasks are serialized to `todos.json` and deserialized back into Task objects on startup

Requirements

- Python 3.8+

Quick start

1. Open a terminal and change into the project directory:

```bash
cd /path/to/min_pro/src
```

2. Run the app:

```bash
python3 main.py
```

Notes on JSON <-> Objects conversion

- Serialization: Task instances are converted to dictionaries (primitive types only) and written to `todos.json` using `json.dump`.
- Deserialization: On startup the app reads `todos.json` (if present), parses JSON into plain dicts, and constructs Task objects from those dicts (restoring id, title, completed fields).

Repository contents and good practices

- Keep `src/` as the source folder. The running command above assumes `main.py` is in `src/`.
- `todos.json` stores app data. If you want to start with a fresh state, delete or rename that file before launching the app.

How to push this project to GitHub

1. If you haven't already, create a repository on GitHub (via web UI) named e.g. `min_pro`.

2. In your local project root (one level above `src`), run these commands to push: replace `USERNAME` and `REPO` with your values.

```bash
cd /path/to/min_pro
git init
git add .
git commit -m "Initial commit: OOP Todo CLI with JSON persistence"
git branch -M main
# Using HTTPS remote (replace URL):
git remote add origin https://github.com/USERNAME/REPO.git
# Or using SSH remote (if you have SSH keys configured):
# git remote add origin git@github.com:USERNAME/REPO.git
git push -u origin main
```

Alternative: use GitHub CLI to create and push in one flow (if `gh` is installed):

```bash
cd /path/to/min_pro
gh repo create USERNAME/REPO --public --source=. --remote=origin --push
```

Helpful tips

- If push is rejected because repo already has commits, run:

```bash
git pull --rebase origin main
# resolve any conflicts, then
git push
```

- If you prefer to keep your `todos.json` out of the repo (local only), add `src/todos.json` to `.gitignore` (see below). If you want a sample data file included, commit a copy such as `src/todos.sample.json` instead.

Suggested commit message flow

- Use small, descriptive commits that show progress, e.g.:
  - "Add Task model and JSON serialization"
  - "Implement add/view/update/delete in CLI"
  - "Persist tasks to src/todos.json"

License & attribution

- Add a LICENSE file if you intend to open-source the project. MIT is a good, permissive choice for small projects.

Contact / next steps

- If you want, I can prepare a minimal `CONTRIBUTING.md`, add a sample `src/todos.sample.json`, or update `main.py` to include argument flags for advanced usage.
