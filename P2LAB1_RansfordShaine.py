# Shaine Ransford
# 2/26/2024
# P2LAB1
# This program will compute the cost of gas for a set distance

# Variables/Input

gasMileage = float(input("Enter your gas mileage: "))
gasPrice = float(input("Enter the cost of gas: "))

# Calculations

per_Mile = gasPrice / gasMileage

cost20 = per_Mile * 20
cost75 = per_Mile * 75
cost500 = per_Mile * 500

# Output

print()
print(f'{cost20:.2f}')
print(f'{cost75:.2f}')
print(f'{cost500:.2f}')
