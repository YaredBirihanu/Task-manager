from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'Pending'

    def __str__(self):
        return f"[{self.status}] {self.title} - Due: {self.due_date.strftime('%Y-%m-%d')}"

    def mark_completed(self):
        self.status = 'Completed'


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                self.tasks.remove(task)
                print(f"Task '{task.title}' removed.")
                return
        print("Task not found.")

    def update_task(self, title, new_title=None, new_description=None, new_due_date=None):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_due_date:
                    task.due_date = new_due_date
                print(f"Task '{title}' updated.")
                return
        print("Task not found.")

    def list_tasks(self):
        return [str(task) for task in self.tasks if task]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_completed()
                print(f"Task '{task.title}' marked as completed.")
                return
        print("Task not found.")


class FrontendManager:
    def __init__(self):
        self.task_manager = TaskManager()

    def run(self):
        while True:
            print("\n--- Task Management System ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Update Task")
            print("4. List Tasks")
            print("5. Mark Task as Completed")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date_str = input("Enter due date (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                task = Task(title, description, due_date)
                self.task_manager.add_task(task)

            elif choice == '2':
                title = input("Enter task title to remove: ")
                self.task_manager.remove_task(title)

            elif choice == '3':
                title = input("Enter task title to update: ")
                new_title = input("Enter new title (or press Enter to skip): ")
                new_description = input("Enter new description (or press Enter to skip): ")
                new_due_date_str = input("Enter new due date (YYYY-MM-DD or press Enter to skip): ")
                new_due_date = datetime.strptime(new_due_date_str, '%Y-%m-%d') if new_due_date_str else None
                self.task_manager.update_task(title, new_title if new_title else None,
                                               new_description if new_description else None,
                                               new_due_date)

            elif choice == '4':
                tasks = self.task_manager.list_tasks()
                print("\nTasks:")
                for task in tasks:
                    print(task)

            elif choice == '5':
                title = input("Enter task title to mark as completed: ")
                self.task_manager.mark_task_completed(title)

            elif choice == '6':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()