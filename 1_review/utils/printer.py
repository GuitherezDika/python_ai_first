def print_todos(todos):
    print("\n=== TODO LIST ===")
    for todo in todos:
        status = "✅" if todo.is_done else "❌"
        print(f"{todo.id}. {todo.name} - {todo.task} [{status}]")
    print("=================\n")