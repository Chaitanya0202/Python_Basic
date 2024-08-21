# Finding The HCF Of Two Number Using The function
def function1(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
print(function1(16, 64))