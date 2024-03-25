# Shaine Ransford
# 3/13/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
add = sum(grades)
amount = len(grades)
avg = add / amount

# Determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80 and avg < 90:
    print('Your grade is: B')
elif avg >= 70 and avg < 80:
    print('Your grade is: C')
elif avg >= 60 and avg < 70:
    print('Your grade is: D')
elif avg < 60:
    print('Your grade is: F') 





