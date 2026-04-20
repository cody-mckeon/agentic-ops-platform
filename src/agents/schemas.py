from enum import Enum

from pydantic import BaseModel, Field


class TaskType(str, Enum):
    WEB_ANALYTICS_WEEKLY_CHANGE = "web_analytics.weekly_change"
    UNSUPPORTED = "unsupported"


class UserRequest(BaseModel):
    message: str = Field(..., min_length=1)


class RouteResult(BaseModel):
    task_type: TaskType
    reason: str
