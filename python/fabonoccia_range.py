print("Program for fobaniccia sereis ")
n = int(input("Enter the Nth number :"))
num1=0
num2=1
# print(num1,num2)
print("febbocin series is :",num1,num2,end=" ")
for i in range(2,n):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
print()