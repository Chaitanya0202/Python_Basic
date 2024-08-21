num = int(input("Enter the value: "))
sum = 0
temp = num

while num > 0:
    digit = num % 10
    sum += digit**3  # Accumulate the sum of cubes
    num = num // 10  # Use integer division to remove the last digit

if temp == sum:
    print("The number is an Armstrong Number")
else:
    print("Not an Armstrong Number")
