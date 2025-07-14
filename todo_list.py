
# To-Do List Application (CLI)
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task(input("Enter task: "))
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task(int(input("Enter task number to delete: ")))
    elif choice == "4":
        break
