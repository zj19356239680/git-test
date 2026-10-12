"""Command-line interface for the Git course demo."""

from __future__ import annotations

import argparse

from task_manager import Task, TaskManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A tiny command-line task manager")
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    list_parser = commands.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--all",
        action="store_true",
        help="Include completed tasks",
    )

    done_parser = commands.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("id", type=int, help="Task ID")

    rename_parser = commands.add_parser("rename", help="Rename a task")
    rename_parser.add_argument("id", type=int, help="Task ID")
    rename_parser.add_argument("title", help="New task title")

    remove_parser = commands.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("id", type=int, help="Task ID")

    return parser


def format_task(task: Task) -> str:
    marker = "x" if task.completed else " "
    return f"[{marker}] {task.id}: {task.title}"


def main() -> int:
    args = build_parser().parse_args()
    manager = TaskManager()

    try:
        if args.command == "add":
            task = manager.add_task(args.title)
            print(f"Added: {format_task(task)}")
        elif args.command == "list":
            tasks = manager.list_tasks(include_completed=args.all)
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                print(format_task(task))
        elif args.command == "done":
            task = manager.complete_task(args.id)
            print(f"Completed: {format_task(task)}")
        elif args.command == "rename":
            task = manager.rename_task(args.id, args.title)
            print(f"Renamed: {format_task(task)}")
        elif args.command == "remove":
            task = manager.remove_task(args.id)
            print(f"Removed: {format_task(task)}")
    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

