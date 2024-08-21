class student:
    def studentdetail(self):
        return f"the name of the student is {self.name} ,roll number is {self.rollno} and    fev subject is {self.fevsub}"
std1 = student()
std2 = student()

std1.name = "std1"
std1.rollno = 65
std1.fevsub = "math"

std2.name = "std2"
std2.rollno = 45
std2.fevsub = "physics"

print(std1.studentdetail())