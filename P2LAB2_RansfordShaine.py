# Shaine Ransford

# 2/26/2024

# P2LAB2   

# This program will calculate the product and average of 4 user input numbers.
# They will be displayed as integers then floats.

# Variables / Inputs

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculations

numProdF = num1 * num2 * num3 * num4

numAdd = num1 + num2 + num3 + num4
numAvgF = numAdd / 4

# Output

print(f'{numProdF:.0f} {numAvgF:.0f}')
print(f'{numProdF:.3f} {numAvgF:.3f}')
