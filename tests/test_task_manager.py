import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager


class TaskManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        storage_path = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(storage_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_and_list_tasks(self) -> None:
        task = self.manager.add_task("Learn Git")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Learn Git")
        self.assertEqual(self.manager.list_tasks(), [task])

    def test_complete_task(self) -> None:
        task = self.manager.add_task("Create a branch")

        completed = self.manager.complete_task(task.id)

        self.assertTrue(completed.completed)
        self.assertEqual(self.manager.list_tasks(include_completed=False), [])

    def test_remove_task(self) -> None:
        task = self.manager.add_task("Merge a feature")

        removed = self.manager.remove_task(task.id)

        self.assertEqual(removed, task)
        self.assertEqual(self.manager.list_tasks(), [])

    def test_rename_task(self) -> None:
        task = self.manager.add_task("Draft release notes")

        renamed = self.manager.rename_task(task.id, "  Publish release notes  ")

        self.assertEqual(renamed.title, "Publish release notes")
        self.assertEqual(self.manager.list_tasks(), [renamed])

    def test_reject_empty_renamed_title(self) -> None:
        task = self.manager.add_task("Keep this title")

        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            self.manager.rename_task(task.id, "   ")

        self.assertEqual(self.manager.list_tasks(), [task])

    def test_reject_empty_title(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            self.manager.add_task("   ")

    def test_unknown_task_id(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not exist"):
            self.manager.complete_task(99)


if __name__ == "__main__":
    unittest.main()

