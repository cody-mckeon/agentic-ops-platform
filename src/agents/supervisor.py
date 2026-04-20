from agents.routing import route_request
from agents.schemas import RouteResult, UserRequest


class SupervisorAgent:
    def handle(self, request: UserRequest) -> RouteResult:
        return route_request(request.message)
