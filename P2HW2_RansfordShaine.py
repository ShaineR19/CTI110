# Shaine Ransford

# 2/26/2024

# P2LAB2   

# This program will ask the user to enter grade for there tests.
# Then it will display the lowest grade, highest grade, sum of grades and the grade average.


# Inputs

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Variables

module_test_grades = [mod1, mod2, mod3, mod4, mod5, mod6]
lowest_grade = min(module_test_grades)
highest_grade = max(module_test_grades)
sum_grades = sum(module_test_grades)
amount_grades = len(module_test_grades)

# Calculations

avg_grades = sum_grades / amount_grades

# Output

print()
print("              Results:")
print("Lowest Grade:   ", lowest_grade)
print("Highest Grade:  ", highest_grade)
print("Sum of Grades:  ", sum_grades)
print("Average:        ", avg_grades)
