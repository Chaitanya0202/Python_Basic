class employee:
    def printdetail(self):
        return f"name is {self.name} salary is {self.salary} and role is {self.role}"
sandy = employee()
suresh = employee()

sandy.name = "sandy"
sandy.salary = 2334
sandy.role = "worker"
suresh.name = "suresh"
suresh.salary = 4564
suresh.role = "security"

print(sandy.printdetail())


