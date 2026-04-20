from agents.schemas import UserRequest
from agents.supervisor import SupervisorAgent


def main() -> None:
    supervisor = SupervisorAgent()

    request = UserRequest(message="What changed in web performance this week?")
    result = supervisor.handle(request)

    print("Task:", result.task_type.value)
    print("Reason:", result.reason)


if __name__ == "__main__":
    main()
