from agents.schemas import RouteResult, TaskType


WEB_ANALYTICS_TERMS = {
    "web performance",
    "site performance",
    "analytics",
    "traffic",
    "pageviews",
    "sessions",
    "conversion",
}

CHANGE_TERMS = {
    "what changed",
    "changed",
    "this week",
    "weekly",
    "week over week",
    "wow",
}


def route_request(message: str) -> RouteResult:
    text = message.strip().lower()

    has_web_analytics_intent = any(term in text for term in WEB_ANALYTICS_TERMS)
    has_change_intent = any(term in text for term in CHANGE_TERMS)

    if has_web_analytics_intent and has_change_intent:
        return RouteResult(
            task_type=TaskType.WEB_ANALYTICS_WEEKLY_CHANGE,
            reason="Matched web analytics and weekly change intent.",
        )

    return RouteResult(
        task_type=TaskType.UNSUPPORTED,
        reason="No supported v1 route matched.",
    )
