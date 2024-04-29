#Shaine Ransford
#4/22/2024
#P5HW
#Math Quiz Generator

import random

def option_1():
    print()
    guessCount = 1
    
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    add = num1 + num2
    
    print("  ", num1)
    print(" +", num2)
    print("-----")
    user = int(input("Enter Answer: "))
    
    while (user != add):
        if(user < add):
            print("Sorry. Your answer is too low.")
            print()
        elif(user > add):
            print("Sorry. Your answer is too high.")
            print()
            
        guessCount += 1
        user = int(input("Try again: "))
    print()    
    print("Congratulations! Your answer is correct!")
    print("Number of guesses: ", guessCount)
    print()
    
    menu()
    
            
def option_2():
    print()
    guessCount = 1
    
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    add = num1 - num2
    
    print("  ", num1)
    print(" -", num2)
    print("-----")
    user = int(input("Enter Answer: "))
    
    while (user != add):
        if(user < add):
            print("Sorry. Your answer is too low.")
            print()
        elif(user > add):
            print("Sorry. Your answer is too high.")
            print()
            
        guessCount += 1
        user = int(input("Try again: "))
    print()    
    print("Congratulations! Your answer is correct!")
    print("Number of guesses: ", guessCount)
    print()
    
    menu()
    
def display_menu():
    print("Welcome to the Math Quiz")
    print()
    print("MAIN MENU")
    print("-------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    userInput = int(input("Please choose an option: "))
    return userInput
    
def menu():
    user = 0
    user = display_menu()
    while(user > 3 or user < 1):
        print("Please enter a valid number")
        user = int(input("Please choose an option 1-3: "))
    if(user == 1):
        print()
        option_1()
    elif(user == 2):
        print()
        option_2()
    elif(user == 3):
        print()
        print("Thank you for playing...")
        print("Bye!!")
    
def main():
    menu()
    
main()
