# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:14:45 2025

@author: pkhan
"""

#Test code

while True:
    # Ask if the user wants to continue or exit
    exit_input = input("Type 'good bye' to exit or press Enter to continue:\n").strip().lower()
    if exit_input == "good bye":
        print("Exiting the calculator. Goodbye!")
        break

    # Taking input from the user
    x = int(input("Enter the first number:\n"))
    y = int(input("Enter the second number:\n"))

    # Displaying the menu
    print("Enter your choice from the menu list:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5 Exponential") 
    
    # Taking the user's choice
    choice = int(input("Enter your choice:\n"))

    # Performing the operation based on the choice
    if choice == 1:
        print("The sum of the two numbers is:", x + y)
    elif choice == 2:
        print("The difference of the two numbers is:", x - y)
    elif choice == 3:
        print("The product of the two numbers is:", x * y)
    elif choice == 4:
        if y == 0:
            print("Indeterminate error: Division by zero")
        else:
            print("The quotient is:", x / y)
    elif choice==5:
        print("The exponential of the two numbers is:", x**y)
    else:
            print("The entered choice does not exist.")

#For loop
x= "Prince Robotics"
for z in x:
    print(z)
    
y= " 1782386703"
for Z in y:
    print(Z)

for i in range(30):
    print(i)
    
for i in range(30,43,2):
    print(i)    
for i in range(100,1,-1):
    print (i)
    