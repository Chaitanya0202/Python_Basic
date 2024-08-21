from collections import Counter

# Input number of shoes and their sizes
numShoes = int(input("Enter the number of shoes: "))
shoes = Counter(map(int, input("Enter the shoe sizes: ").split()))

# Input number of customers
numCust = int(input("Enter the number of customers: "))

income = 0

# Process each customer's request
for _ in range(numCust):
    size, price = map(int, input("Enter shoe size and price: ").split())
    if shoes[size] > 0: 
        income += price  
        shoes[size] -= 1 

print("Total income:", income)
