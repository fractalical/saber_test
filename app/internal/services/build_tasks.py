__all__ = [
    "Tasks",
]

from typing import List
import yaml

from app.pkg import models


class Tasks:

    @staticmethod
    async def read_builds_file(cmd: models.BuildName) -> models.BuildTasks:
        with open('builds\\builds.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        build_tasks = []
        for build in data['builds']:
            if build['name'] == cmd.name:
                # build_name = build['name']
                build_tasks = [task for task in build['tasks']]
                # tasks = [task for task in build['tasks']]
                # builds[build_name] = tasks

        return models.BuildTasks(tasks=build_tasks)

    @staticmethod
    async def read_tasks(build_tasks: models.BuildTasks) -> list[models.Task]:
        # читаем yaml файл
        with open("builds\\tasks.yaml", "r") as f:
            tasks = yaml.safe_load(f)

        # создаем словарь вида {"task_name": [dependency_1, dependency_2, ...]}
        result = []
        for task in tasks["tasks"]:
            # print('task_name', task["name"])
            # print('build_tasks.tasks', build_tasks.tasks)
            if task["name"] in build_tasks.tasks:
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

    @staticmethod
    async def topological_sort(tasks: list[models.Task]) -> models.BuildTasks:
        # Создаем словарь для хранения зависимостей каждой задачи
        # Создаем множество для хранения невыполненных задач
        # Создаем список для хранения отсортированных задач
        remaining_tasks = set()
        dependencies = dict()
        for task in tasks:
            remaining_tasks.add(task.name)
            dependencies[task.name] = set(task.dependencies)
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
                raise ValueError('Circular dependency detected')
            # Добавляем найденную задачу в список отсортированных задач

            # sorted_tasks.extend([models.TaskName(name=t) for t in sorted(ready_tasks)])
            # sorted_tasks.tasks.extend(sorted(ready_tasks))
            sorted_tasks.extend(sorted(ready_tasks))
            # Удаляем найденную задачу из множества невыполненных задач
            remaining_tasks.difference_update(ready_tasks)
            # Удаляем найденную задачу из зависимостей оставшихся задач
            for task in remaining_tasks:
                dependencies[task].difference_update(ready_tasks)
        print('SORTED LIST', sorted_tasks)
        return models.BuildTasks(tasks=sorted_tasks)

    async def get_build_tasks(self, cmd: models.BuildName) -> models.BuildTasks:

        build_tasks = await self.read_builds_file(cmd)
        print('build_tasks', build_tasks)
        tasks = await self.read_tasks(build_tasks)
        print('tasks', tasks)
        sort_tasks = await self.topological_sort(tasks)
        print('sort_tasks', sort_tasks)

        return sort_tasks
