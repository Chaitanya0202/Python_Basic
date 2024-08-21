class employee:

    def __init__(self,aname,asalary,aroll):
        self.name=aname
        self.salary = asalary
        self.roll = aroll
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary} and role is {self.roll}"
sandy = employee("sandy",255,"worker")
print(sandy.printdetails())