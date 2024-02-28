# Shaine Ransford

# 02/14/2024

# P1HW2

# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")

# Input
print()
budget = float(input("Enter Budget: " ))
print()
spot = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("How much will you need for accomodation/hotel? "))
print()
food = float(input("How much do you need for food? "))
print()

# Calculations

expenses = gas + hotel + food
leftover = budget - expenses

# Output

print("-------Travel Expenses--------")
print("Location:         ", spot)
print("Initial Budget:    $"f'{budget:.2f}')
print("Fuel:              $"f'{gas:.2f}')
print("Accomodation:      $"f'{hotel:.2f}')
print("Food:              $"f'{food:.2f}')
print("------------------------------")
print()
print("Remaining balance: $"f'{leftover:.2f}')
