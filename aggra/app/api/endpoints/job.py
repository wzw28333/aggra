import inspect
from typing import List, get_type_hints
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
        args = inspect.getfullargspec(v.run)
        args_meta = {
            "args": args.args,
            "defaults": args.defaults,
            "varargs": args.varargs,
            "varkw": args.varkw,
            "kwonlyargs": args.kwonlyargs,
            "kwonlydefaults": args.kwonlydefaults,
            "annotations": {
                k: str(v)
                for k, v in args.annotations.items()
            },
        }
        job = Job(
            job_name=k,
            name=v.__name__,
            module=v.__module__,
            description=inspect.getdoc(v),
            max_retries=v.max_retries,
            rate_limit=v.rate_limit,
            ignore_result=v.ignore_result,
            expires=v.expires,
            priority=v.priority,
            args_meta=args_meta,
        )
        jobs.append(job)
    return jobs
