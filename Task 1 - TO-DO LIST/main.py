import json
from datetime import datetime

TODO_FILE = "todo.json"


def load_data():
    try:
        with open(TODO_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"tasks": [], "next_id": 1}
    return data


def save_data(data):
    with open(TODO_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def add_task(name, description):
    data = load_data()
    tasks = data["tasks"]
    next_id = data["next_id"]

    current_date = datetime.now().strftime("%Y-%m-%d")
    new_task = {
        'id': next_id,
        'name': name,
        'description': description,
        'due_date': current_date,
        'completed': False
    }
    tasks.append(new_task)
    data["next_id"] = next_id + 1
    save_data(data)
    return new_task


def remove_task(task_id):
    data = load_data()
    tasks = data["tasks"]
    removed_task = None

    new_tasks = [task for task in tasks if task['id'] != task_id]

    if len(new_tasks) < len(tasks):
        removed_task = tasks[task_id - 1]  # Get the task before removal for return

        for i, task in enumerate(new_tasks, start=1):
            task['id'] = i

        data["tasks"] = new_tasks
        data["next_id"] = len(new_tasks) + 1
        save_data(data)

    return removed_task


def list_tasks():
    data = load_data()
    tasks = data["tasks"]
    return tasks


def mark_task_completed(task_id):
    data = load_data()
    tasks = data["tasks"]
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_data(data)
            return task

    return None


def main():
    print("Welcome to the To-Do List App!")

    while True:
        print("\nAvailable commands:")
        print("1. add")
        print("2. remove")
        print("3. list")
        print("4. complete")
        print("5. exit")

        command = input("Enter a command: ").strip().lower()

        if command == 'add':
            name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            add_task(name, description)
            print(f"Task '{name}' added successfully.")
        elif command == 'remove':
            task_id = int(input("Enter the ID of the task to remove: ").strip())
            removed_task = remove_task(task_id)
            if removed_task:
                print(f"Task '{removed_task['name']}' with ID '{task_id}' removed successfully.")
            else:
                print(f"Task with ID '{task_id}' not found.")
        elif command == 'list':
            tasks = list_tasks()
            if tasks:
                print("Current tasks:")
                for task in tasks:
                    status = "Done" if task['completed'] else "Pending"
                    print(f"ID: {task['id']} - {task['name']} - {task['description']} - Due: {task['due_date']} - Status: {status}")
            else:
                print("No tasks found.")
        elif command == 'complete':
            task_id = int(input("Enter the ID of the task to mark as completed: ").strip())
            completed_task = mark_task_completed(task_id)
            if completed_task:
                print(f"Task '{completed_task['name']}' with ID '{task_id}' marked as completed.")
            else:
                print(f"Task with ID '{task_id}' not found.")
        elif command == 'exit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
