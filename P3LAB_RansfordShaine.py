# Shaine Ransford
# 3/11/2024
# P3LAB1
# This project will calculate the exact coinage of a given change amount
 
# Variables
penny = int()
nickel = int()
dime = int()
quarter = int()
dollar = int()
price = int(-1)

# Input
while price < 0:
    price = int(input("What is the total change amount?"))

# Calculations
if price == 0:
    print("No change")
    
if price > 0:
    # Dollar Amount
    dollar = price // 100
    price = price % 100
    
    # Quarter Amount
    quarter = price // 25
    price = price % 25
    
    # Dime Amount
    dime = price // 10
    price = price % 10
    
    # Nickel Amount
    nickel = price // 5
    price = price % 5
    
    # Penny Amount
    penny = price // 1
    price = price % 1
    
# Output

# Dollars
if dollar > 1:
    print(dollar, "Dollars")
elif dollar == 1:
    print(dollar, "Dollar")
    
# Quarters    
if quarter > 1:
    print(quarter, "Quarters")
elif quarter == 1:
    print(quarter, "Quarter")
    
# Dimes
if dime > 1:
    print(dime, "Dimes")
elif dime == 1:
    print(dime, "Dime")
    
# Nickels
if nickel > 1:
    print(nickel, "Nickels")
elif nickel == 1:
    print(nickel, "Nickel")
    
# Pennies
if penny > 1:
    print(penny , "Pennies")
elif penny == 1:
    print(penny, "Penny")
    
