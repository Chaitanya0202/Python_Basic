n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
z= input()
y=(student_marks[z])
sum=0
for j in y:
    sum+=j
    avg=sum/3
print("{0:.2f}".format(avg))