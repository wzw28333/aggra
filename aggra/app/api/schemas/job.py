from typing import Any
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Job(BaseModel):
    job_name: str
    name: str
    module: str
    description: Optional[str]
    max_retries: Optional[int]
    rate_limit: Optional[str]
    ignore_result: Optional[bool]
    expires: Optional[datetime]
    priority: Optional[int]
    # typing hints
    args_meta: Optional[dict]