from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.internal import services
from app.pkg import models

router = APIRouter(prefix="/build", tags=["Build"])


@router.post(
    '/get_tasks',
    response_model=List[str],
    status_code=status.HTTP_200_OK,
    summary="Get tasks of build.",
)
@inject
async def registration(
        build: models.BuildName,
        get_tasks: services.Tasks = Depends(Provide[services.Services.tasks])
):
    tasks = await get_tasks.get_build_tasks(build)
    return tasks.tasks
