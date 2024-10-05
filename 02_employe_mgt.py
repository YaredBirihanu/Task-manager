
import csv

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Salary: ${self.salary:.2f})"

    def format_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary:.2f}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return [str(emp) for emp in self.employees]

    def delete_employees_in_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

    def update_employee_salary(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
            return True
        return False

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Salary'])  # Header
            for emp in self.employees:
                writer.writerow([emp.name, emp.age, emp.salary])
        print("Employee data saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.employees = [Employee(name, int(age), float(salary)) for name, age, salary in reader]
            print("Employee data loaded from file.")
        except FileNotFoundError:
            print("File not found. Please ensure the file exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\n--- Employee Management System ---")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete Employees by Age Range")
            print("4. Find Employee by Name")
            print("5. Update Employee Salary")
            print("6. Save Employees to File")
            print("7. Load Employees from File")
            print("8. Exit")

            choice = input("Choose an option (1-8): ")

            if choice == '1':
                name = input("Enter employee name: ")
                age = int(input("Enter employee age: "))
                salary = float(input("Enter employee salary: "))
                employee = Employee(name, age, salary)
                self.manager.add_employee(employee)
                print("Employee added successfully.")

            elif choice == '2':
                employees = self.manager.list_employees()
                if employees:
                    print("\nEmployees List:")
                    for emp in employees:
                        print(emp)
                else:
                    print("No employees found.")

            elif choice == '3':
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                self.manager.delete_employees_in_age_range(min_age, max_age)
                print("Employees deleted successfully.")

            elif choice == '4':
                name = input("Enter employee name to search: ")
                employee = self.manager.find_employee_by_name(name)
                if employee:
                    print(employee)
                else:
                    print("Employee not found.")

            elif choice == '5':
                name = input("Enter employee name to update salary: ")
                new_salary = float(input("Enter new salary: "))
                if self.manager.update_employee_salary(name, new_salary):
                    print("Salary updated successfully.")
                else:
                    print("Employee not found.")

            elif choice == '6':
                filename = input("Enter filename to save: ")
                self.manager.save_to_file(filename)

            elif choice == '7':
                filename = input("Enter filename to load: ")
                self.manager.load_from_file(filename)

            elif choice == '8':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__=='__main__':
    frontend=FrontendManager()
    frontend.run()