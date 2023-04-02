import yaml

from app.pkg import models


class Build:

    @staticmethod
    async def read_builds_file() -> models.BuildTasks:
        with open('builds.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        builds = {}
        for build in data['builds']:
            build_name = build['name']
            tasks = [task for task in build['tasks']]
            builds[build_name] = tasks

        return builds
