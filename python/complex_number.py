num = int(input("Enter a number: "))  # Input the number
temp = num
s = 0

# Calculate the sum of digits
while num != 0:
    digit = num % 10  
    s += digit  
    num = num // 10  

# Check if the original number is divisible by the sum of its digits
if temp % s == 0:
    print("YES")  
else:
    print("NO")  
