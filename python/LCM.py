
def function1(x,y):
    
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater += 1
    return lcm
num1=54
num2=24
print(function1(num1,num2))