# Shaine Ransford
# 3/25/2024
# P4HW1
# This program will collect a user's scores nad display them back to the user

amount = int(input("How many scores do you want to enter? "))

# create list
scoreList = [amount]
# Take the users input for each score
while amount > 0:
    for i in range(len(scoreList)):
        score = int(input("Enter score #", i ,":"))
    amount = amount - 1
    print(amount)
#
