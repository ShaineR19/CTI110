# Shaine Ransford
# 3/20/2024
# P3HW2
# This program will calculate a user's salary given their hours worked and pay rate.

# Variables

# Input
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# Calculations
if (hours > 40.0):
    overtime = hours - 40.0
    overtimePay = overtime * rate
    pay = 40.0 * rate
    gross = pay + overtimePay
else:
    overtime = 0.0
    overtimePay = overtime * rate
    pay = hours * rate
    gross = pay + overtimePay

# Output
print("---------------------------------------------------------------------------------")
print("Employee name:  ", name)
print()
print("Hours Worked   Pay Rate   Overtime   Overtime Pay      RegHour Pay      Gross Pay")
print("---------------------------------------------------------------------------------")
print(hours, "         ", rate, "     ", overtime, "      ", "$",overtimePay, "          ", "$",pay, "        ","$",gross)
