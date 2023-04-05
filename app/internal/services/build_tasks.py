from pprint import pprint
from typing import List

import yaml

from app.configuration.logger_settings import app_log
from app.pkg import models
from app.pkg.models.exceptions import (BuildNotFound, CircularDependency,
                                       EmptyBuildName, NotFoundTask)

__all__ = [
    "Tasks",
]


class Tasks:

    @staticmethod
    async def read_builds_file(cmd: models.BuildName) -> models.BuildTasks:
        with open('builds/builds.yaml', 'r') as file:
            data = yaml.safe_load(file)

        for build in data['builds']:
            if build['name'] == cmd.build:
                build_tasks = build['tasks']

                return models.BuildTasks(tasks=build_tasks)
        else:
            app_log.error(f"404 Build {cmd.build} not found.")
            raise BuildNotFound

    @staticmethod
    async def read_tasks(build_tasks: models.BuildTasks) -> List[models.Task]:

        # читаем yaml файл
        with open("builds/tasks.yaml", "r") as file:
            tasks = yaml.safe_load(file)

        # создаем словарь вида {"task_name": [dependency_1, dependency_2, ...]}
        result = []
        for task in tasks["tasks"]:
            if task["name"] in build_tasks.tasks:
                result.append(models.Task(
                    name=task["name"],
                    dependencies=task.get("dependencies", [])
                ))
        if len(result) != len(build_tasks.tasks):
            raise NotFoundTask

        return result

    @staticmethod
    async def topological_sort(tasks: List[models.Task]) -> models.BuildTasks:

        # Создаем множество для хранения невыполненных задач
        remaining_tasks = set()
        # Создаем словарь для хранения зависимостей каждой задачи
        dependencies = dict()
        for task in tasks:
            remaining_tasks.add(task.name)
            dependencies[task.name] = set(task.dependencies)
        # Создаем список для хранения отсортированных задач
        sorted_tasks = []
        # убираем из зависимостей задачи, которых нет в списке билда
        for task in dependencies:
            dependencies[task].intersection_update(remaining_tasks)

        while remaining_tasks:
            # Ищем задачу, у которой все зависимости уже выполнены
            ready_tasks = [task for task in remaining_tasks if
                           not dependencies[task]]
            if not ready_tasks:
                # Если таких задач нет, значит есть циклическая зависимость
                app_log.warning(f"508 Circular dependency detected.")
                raise CircularDependency
            # Добавляем найденную задачу в список отсортированных задач
            sorted_tasks.extend(sorted(ready_tasks))
            # Удаляем найденную задачу из множества невыполненных задач
            remaining_tasks.difference_update(ready_tasks)
            # Удаляем найденную задачу из зависимостей оставшихся задач
            for task in remaining_tasks:
                dependencies[task].difference_update(ready_tasks)
        return models.BuildTasks(tasks=sorted_tasks)

    async def get_build_tasks(self, cmd: models.BuildName) -> models.BuildTasks:

        if not cmd.build:
            app_log.error(f"400 Empty build name.")
            raise EmptyBuildName

        build_tasks = await self.read_builds_file(cmd)
        tasks = await self.read_tasks(build_tasks)
        sort_tasks = await self.topological_sort(tasks)

        return sort_tasks
