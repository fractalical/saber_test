from typing import List

import yaml

from app.pkg import models


class TasksRead:

    @staticmethod
    async def read_tasks(build: models.BuildTasks) -> List[models.Task]:
        # читаем yaml файл
        with open("tasks.yaml", "r") as f:
            tasks = yaml.safe_load(f)

        # создаем словарь вида {"task_name": [dependency_1, dependency_2, ...]}
        result = []
        for task in tasks["tasks"]:
            if task["name"] in build:
                result.append(models.Task(
                    name=task["name"],
                    dependencies=task.get("dependencies", [])
                ))
                # result.append(
                #     {
                #         "name": task["name"],
                #         "dependencies": task.get("dependencies", [])
                #     }
                # )

        return result
