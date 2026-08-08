def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter your task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def update_task(tasks):
    if not tasks:
        print("No tasks available to update.")
        return

    display_tasks(tasks)
    choice = input("Enter the task number to update: ")
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return

    new_task = input("Enter the new task description: ").strip()
    if not new_task:
        print("Task description cannot be empty.")
        return

    tasks[index] = new_task
    print("Task updated successfully!")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return

    display_tasks(tasks)
    choice = input("Enter the task number to delete: ")
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return

    removed = tasks.pop(index)
    print(f"Removed task: {removed}")


def main():
    tasks = []

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option from 1 to 5.")


if __name__ == "__main__":
    main()
