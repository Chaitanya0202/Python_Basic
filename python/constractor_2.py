class student:

    def __init__(self,aname,arollno,marks):
        self.name=aname
        self.marks = marks
        self.rollno = arollno
    def studentdetails(self):
         return f"the name is {self.name} ,roll no is {self.rollno} and marks are {self.marks}"
sandy = student("suresh",255,56)
print(sandy.studentdetails())