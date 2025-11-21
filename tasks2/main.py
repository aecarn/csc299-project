#!/usr/bin/env python3
import json
import argparse
from pathlib import Path

# 1) Where the data lives
TASKS_FILE = Path(__file__).parent / "tasks.json"

# 2) Make sure the file exists so we don't crash on first run
def ensure_tasks_file():
    if not TASKS_FILE.exists():
        TASKS_FILE.write_text("[]", encoding="utf-8")  # empty list

# 3) Data helpers (load/save)
def load_tasks():
    ensure_tasks_file()
    with TASKS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)  # JSON -> Python list of dicts

def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)  # Python -> JSON

def next_id(tasks):
    return (max((t["id"] for t in tasks), default=0) + 1)

# 4) Commands
def cmd_add(args):
    tasks = load_tasks()
    new_task = {
        "id": next_id(tasks),
        "title": args.title,
        "description": args.description or "",
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Added #{new_task["id"]}: {new_task["title"]}')

def cmd_list(_args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "✓" if t.get("done") else " "
        print(f'[{t["id"]}] [{status}] {t["title"]} - {t.get("description","")}')


def cmd_search(args):
    tasks = load_tasks()
    q = args.query.lower()
    hits = [
        t for t in tasks
        if q in t["title"].lower() or q in t.get("description","").lower()
    ]
    if not hits:
        print("No matches.")
        return
    for t in hits:
        print(f'[{t["id"]}] {t["title"]} - {t.get("description","")}')

def cmd_done(args):
    tasks = load_tasks()
    tid = args.id
    for t in tasks:
        if t["id"] == tid:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked task #{tid} as done.")
            return
    print(f"No task with id {tid}.")

# 5) Command-line parser (defines add/list/search)
def build_parser():
    p = argparse.ArgumentParser(description="Task manager using tasks.json")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add", help="Add a new task")
    pa.add_argument("title")
    pa.add_argument("-d", "--description")
    pa.set_defaults(func=cmd_add)

    pl = sub.add_parser("list", help="List all tasks")
    pl.set_defaults(func=cmd_list)

    ps = sub.add_parser("search", help="Search tasks")
    ps.add_argument("query")
    ps.set_defaults(func=cmd_search)

    pd = sub.add_parser("done", help="Mark a task as completed")
    pd.add_argument("id", type=int)
    pd.set_defaults(func=cmd_done)

    return p

def main():
    args = build_parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
