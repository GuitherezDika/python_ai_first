from main1_refactored import TodoRepository, TodoService, print_todos

if __name__ == "__main__":
  repo = TodoRepository()
  service = TodoService(repo)

  # Create
  service.create_todo("dika", "read")
  service.create_todo("kaka", "write")
  service.create_todo("mama", "teach")

  print_todos(service.list_todos())

  # Update (mark done)
  service.complete_todo(2)

  # Delete
  service.delete_todo(1)

  print_todos(service.list_todos())