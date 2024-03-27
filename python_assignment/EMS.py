class Employee:
    def __init__(self, name:str, ID:int, title:str, department:str) -> None:
        # Initialize employee details
        self._name = name
        self._ID = ID
        self._title = title
        self._department = department

    @property
    def name(self) -> str:
        return self._name

    @property
    def ID(self) -> int:
        return self._ID

    @property
    def title(self) -> str:
        return self._title

    @property
    def department(self) -> str:
        return self._department

    def display_details(self):
        # Display employee details
        return f"Name : {self.name}, ID : {self.ID}, Title : {self.title}, Department : {self.department}"

    def __str__(self) -> str:
        # String representation of Employee object
        return f"{self.name} - {self.ID}"
    

class Department:
    def __init__(self, department_name:str) -> None:
        # Initialize department with name and empty list of employees
        self._department_name = department_name
        self._employees = []

    @property
    def department_name(self) -> str:
        return self._department_name

    @property
    def employees(self) -> list:
        return self._employees

    def add_employee(self, employee : Employee):
        # Add an employee to the department
        self.employees.append(employee)
        print(f"Employee added succesfully to {self._department_name}")
        employee.display_details()

    def remove_employee(self, employee_id : int):
        # Remove an employee from the department by ID
        self.employees = [employee for employee in self.employees if employee.ID != employee_id]
        print(f"Employee with Id {employee_id} removed succesfully from {self._department_name}")

    def list_employees(self):
        # Display details of all employees in the department
        for employee in self.employees:
            employee.display_details()


class Company:
    def __init__(self) -> None:
        # Initialize company with empty dictionary of departments
        self._departments = {}

    @property
    def departments(self) -> dict:
        return self._departments

    def add_department(self, department):
        # Add a department to the company
        self.departments[department.department_name] = department
    
    def remove_department(self, department_name):
        # Remove a department from the company by name
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            print("Department not found.")

    def display_departments(self):
        # Display all departments and their employees
        for department_name, department in self.departments.items():
            print(f"Department : {department_name}")
            department.list_employees()


def menu(company):
    # Display menu options and handle user input
    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Departments")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Add new employee to a department
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")
            employee = Employee(name, emp_id, title, department)
            if department in company._departments:
                company._departments[department].add_employee(employee)
            else:
                print("Department does not exist.")
        
        elif choice == "2":
            # Remove employee from all departments by ID
            emp_id = input("Enter employee ID to remove: ")
            for department in company._departments.values():
                department.remove_employee(emp_id)
        
        elif choice == "3":
            # Display all departments and their employees
            company.display_departments()
        
        elif choice == "4":
            # Exit the program
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


# Main function to create company, departments, and run menu
if __name__ == "__main__":
    # Create a new company
    company = Company()
    department = Department("Engineering")
    print(department._department_name)
    company.add_department(department)

    # Run the menu
    menu(company)
