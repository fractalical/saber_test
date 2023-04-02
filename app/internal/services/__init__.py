from dependency_injector import containers, providers

from .build_tasks import *


class Services(containers.DeclarativeContainer):

    tasks = providers.Factory(
        Tasks,
    )
