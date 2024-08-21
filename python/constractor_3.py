class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The employee's name is {self.name}, the salary is {self.salary}, and the role is {self.role}."

# Creating an instance of the Employee class
harry = Employee("Harry", 143, "Caretaker")

# Printing the details of the employee
print(harry.print_details())
