from typing import Optional
from pydantic import BaseModel


class Job(BaseModel):
    name: str
    description: Optional[str]
