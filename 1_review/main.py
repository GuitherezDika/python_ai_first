from repository.todo_repository import TodoRepository
from service.todo_service import TodoService
from utils.printer import print_todos

if __name__ == "__main__":
    repo = TodoRepository()
    service = TodoService(repo)

    # Create
    service.create_todo("dika", "read")
    service.create_todo("kaka", "write")
    service.create_todo("mama", "teach")
    service.create_todo("tutua", "farm")
    service.create_todo("oppung", "priest")
    service.create_todo("tigan", "dentist")
    service.create_todo("kakung", "civil servants")
    service.create_todo("papa", "IT engineer")

    print_todos(service.list_todos())

    # Update
    service.complete_todo(2)
    service.complete_todo(4)
    service.complete_todo(5)
    service.complete_todo(7)

    # Delete
    service.delete_todo(1)

    print_todos(service.list_todos())