import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks, description):
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    print(f"Task added: {description}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"[{task['id']}] {task['description']} - {status}")

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(tasks, task_id)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()