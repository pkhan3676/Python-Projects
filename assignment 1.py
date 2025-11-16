# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:26:07 2025

@author: pkhan
"""
# simple_chatbot_basic.py

print("Hello! I'm a simple chatbot. Type 'goodbye' to exit.")

while True:
    user_input = input("> ").lower()

    # Exit condition
    if "goodbye" in user_input or "bye" in user_input:
        print("Goodbye!")
        break

    # Greeting
    elif "hello" in user_input or "hi" in user_input:
        print("Hello there!")

    # Math: addition
    elif "plus" in user_input:
        parts = user_input.split()
        if len(parts) >= 5 and parts[0] == "what" and parts[1] == "is":
            try:
                num1 = int(parts[2])
                num2 = int(parts[4])
                print(num1 + num2)
            except ValueError:
                print("I can only add numbers!")
        else:
            print("Try: What is 3 plus 4?")

    # Math: multiplication
    elif "times" in user_input:
        parts = user_input.split()
        if len(parts) >= 5 and parts[0] == "what" and parts[1] == "is":
            try:
                num1 = int(parts[2])
                num2 = int(parts[4])
                print(num1 * num2)
            except ValueError:
                print("I can only multiply numbers!")
        else:
            print("Try: What is 3 times 4?")

    # Unknown input
    else:
        print("I don't understand. Try saying hello or ask a math question.")
