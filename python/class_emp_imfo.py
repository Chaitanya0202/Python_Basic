class Employee:
    # count=0
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
        # Employee.count +=1
    def displaydetail(self):
        return print("name is ",self.name,"the diseis ",self.desig,"the salary is ",self.salary)
e1=Employee("bolt", "fire", 24)
e2=Employee("dut", "hello", 434)
# e2.display.count()
e1.displaydetail()
e2.displaydetail()
print(e1.salary)