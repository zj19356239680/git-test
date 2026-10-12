# Git Course Demo

一个零第三方依赖的 Python 待办事项命令行程序，适合作为 Git 课程作业的练习仓库。

## 功能

- 添加待办事项
- 查看全部或未完成事项
- 标记事项为已完成
- 删除事项
- 使用 JSON 文件保存数据

## 运行环境

- Python 3.10 或更高版本

## 快速开始

```powershell
python app.py add "学习 git status"
python app.py add "创建 feature 分支"
python app.py list
python app.py done 1
python app.py list --all
python app.py remove 2
```

默认数据保存在项目根目录的 `tasks.json` 中，该文件已被 Git 忽略。

## 运行测试

```powershell
python -m unittest discover -s tests -v
```

## 项目结构

```text
.
|-- app.py                    # 命令行入口
|-- task_manager.py           # 核心业务逻辑
|-- tests/
|   `-- test_task_manager.py  # 单元测试
`-- docs/
    `-- GIT_EXERCISE.md       # Git 作业练习步骤
```

Git 练习建议见 [docs/GIT_EXERCISE.md](docs/GIT_EXERCISE.md)。

