from agents.routing import route_request
from agents.schemas import TaskType


def test_route_web_analytics_weekly_change():
    result = route_request("What changed in web performance this week?")
    assert result.task_type == TaskType.WEB_ANALYTICS_WEEKLY_CHANGE


def test_route_unsupported():
    result = route_request("Draft an email to the vendor")
    assert result.task_type == TaskType.UNSUPPORTED
