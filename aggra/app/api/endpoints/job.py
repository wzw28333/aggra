import inspect
from typing import List
from fastapi import APIRouter, Depends

from aggra.app import deps
from aggra.app.base import Aggra
from aggra.app.api.schemas.job import Job

router = APIRouter()


@router.get("/")
def get_job(
        app: Aggra = Depends(deps.get_app)
) -> List[Job]:
    """
    Get all jobs.
    """
    jobs = []
    for k, v in app.celery.tasks.items():
        if k.startswith("celery."):
            continue

        job = Job(
            name=k,
            description=inspect.getdoc(v)
        )
        print(inspect.getfullargspec(v))
        jobs.append(job)
    return jobs
