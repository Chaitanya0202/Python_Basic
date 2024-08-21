def addition(a,b):
    print("the addition is the ",a+b)
def substraction(a,b):
    print("substractuion is the ",a-b)
x,y = map(int,input().split())
choise=input("+ , - , *  ,/ ")
if(choise=="+"):
    addition(x,y)
if(choise=="-"):
    substraction(x,y)
