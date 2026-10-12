# Git 课程作业练习

下面的步骤会留下清晰的 Git 操作记录。请在项目根目录中执行。

## 1. 创建首次提交

```powershell
git status
git add .
git commit -m "chore: initialize task manager demo"
git log --oneline
```

## 2. 在功能分支上开发

```powershell
git switch -c feature/task-priority
```

可以尝试给 `Task` 增加 `priority` 字段，并让 `list` 命令显示优先级。完成后：

```powershell
git add app.py task_manager.py tests/test_task_manager.py
git commit -m "feat: add task priority"
```

## 3. 合并功能分支

```powershell
git switch main
git merge feature/task-priority
git log --oneline --graph --all
```

## 4. 创建版本标签

```powershell
git tag -a v1.0.0 -m "first course demo release"
git tag
```

## 5. 可选：练习解决冲突

1. 从 `main` 创建两个分支。
2. 在两个分支中分别修改 `README.md` 的同一行并提交。
3. 将两个分支依次合并回 `main`。
4. 第二次合并时手动解决冲突，再执行 `git add` 和 `git commit`。

操作前后都可以使用以下命令观察仓库状态：

```powershell
git status
git diff
git diff --staged
git log --oneline --graph --decorate --all
```

> 提示：如果课程要求保留特定数量或命名格式的提交，请优先按照老师给出的规范调整上述步骤。
