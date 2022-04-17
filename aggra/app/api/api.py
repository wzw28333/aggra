from fastapi import APIRouter

from aggra.app.api.endpoints import job

router = APIRouter()

router.include_router(job.router, prefix="/job", tags=["job"])
