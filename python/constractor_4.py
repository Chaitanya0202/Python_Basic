class subject:
    total_sub=5
    def __init__(self,chemistry,physics,maths):
        self.chemistry=chemistry
        self.physics=maths
        self.maths=maths
    def printdetails1(self):
        return f" The chemistry marks is {self.chemistry} ,physics marks is {self.physics} and maths marks is {self.maths}"
    def avgofsub(self):
        print("The Avarage is",(self.chemistry + self.physics + self.maths)/3)
sub=subject(95, 67, 65)
print(sub.printdetails1())
print(sub.avgofsub())
print(sub.chemistry)