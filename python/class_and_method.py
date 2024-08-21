# class and method example
class Employee:
    #here we can define local variable which can use all method
    def printdetails(self):  # ######This is The Method 
        return f"The Name is {self.name} salary is per month {self.salary} and role is {self.role}"
harry=Employee()
larry=Employee()

harry.name="Harry"
harry.salary=10000
harry.role="Assesistance"

larry.name="Larry"
larry.salary=7546
larry.role="Counter"

print(larry.printdetails())