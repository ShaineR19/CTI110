# Shaine Ransford
# 02/14/2024
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")

# Input
budget = float(input("Enter Budget: " ))
spot = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas: "))
hotel = float(input("How much will you need for accomodation/hotel: "))
food = float(input("How much do you need for food: "))

# Calculations
expenses = gas + hotel + food
leftover = budget - expenses

# Output
print("-------Travel Expenses--------")
print("Location:", spot)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation: ", hotel)
print("Food:", food)
print()
print("Remaining balance:", leftover)

