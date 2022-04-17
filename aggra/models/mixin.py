from datetime import datetime
from sqlmodel import SQLModel, Field, DateTime


class Mixin(SQLModel):

    id = Field(int, primary_key=True)
    created_at: datetime = Field(DateTime, index=True)
    updated_at: datetime = Field(DateTime, index=True)
    deleted_at: datetime = Field(DateTime, index=True)
