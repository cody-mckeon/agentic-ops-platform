from pydantic import BaseModel, Field


class KPIComparisonRequest(BaseModel):
    current_week: str = Field(..., description="Week start date in YYYY-MM-DD format")
    previous_week: str = Field(..., description="Week start date in YYYY-MM-DD format")


class MetricDelta(BaseModel):
    metric_name: str
    current_value: float
    previous_value: float
    absolute_delta: float
    percent_delta: float


class KPIComparisonResult(BaseModel):
    current_week: str
    previous_week: str
    metrics: list[MetricDelta]
