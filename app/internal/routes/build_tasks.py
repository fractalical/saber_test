from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.internal import services
from app.pkg import models

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    '/registration',
    response_model=models.BuildTasks,
    status_code=status.HTTP_200_OK,
    summary="Get tasks of build.",
)
@inject
async def registration(
        build: models.BuildName,
        get_tasks: services.Tasks = Depends(Provide[services.Services.tasks])
):
    return await get_tasks.get_build_tasks(build)
