"""Core task management logic for the Git course demo."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskManager:
    def __init__(self, storage_path: str | Path = "tasks.json") -> None:
        self.storage_path = Path(storage_path)

    def list_tasks(self, include_completed: bool = True) -> list[Task]:
        tasks = self._load()
        if include_completed:
            return tasks
        return [task for task in tasks if not task.completed]

    def add_task(self, title: str) -> Task:
        clean_title = self._clean_title(title)
        tasks = self._load()
        next_id = max((task.id for task in tasks), default=0) + 1
        task = Task(id=next_id, title=clean_title)
        tasks.append(task)
        self._save(tasks)
        return task

    def complete_task(self, task_id: int) -> Task:
        tasks = self._load()
        task = self._find(tasks, task_id)
        task.completed = True
        self._save(tasks)
        return task

    def rename_task(self, task_id: int, title: str) -> Task:
        clean_title = self._clean_title(title)
        tasks = self._load()
        task = self._find(tasks, task_id)
        task.title = clean_title
        self._save(tasks)
        return task

    def remove_task(self, task_id: int) -> Task:
        tasks = self._load()
        task = self._find(tasks, task_id)
        tasks.remove(task)
        self._save(tasks)
        return task

    def _load(self) -> list[Task]:
        if not self.storage_path.exists():
            return []

        data = json.loads(self.storage_path.read_text(encoding="utf-8"))
        return [Task(**item) for item in data]

    def _save(self, tasks: list[Task]) -> None:
        self.storage_path.write_text(
            json.dumps([asdict(task) for task in tasks], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    @staticmethod
    def _clean_title(title: str) -> str:
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Task title cannot be empty")
        return clean_title

    @staticmethod
    def _find(tasks: list[Task], task_id: int) -> Task:
        for task in tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task {task_id} does not exist")

