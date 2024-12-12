# Calculator

from math import factorial, sqrt

def menu():
    return """\nWelcome to Calculator! 
Please start by selecting the operation you wish to perform. 
Here are available operations:  
1. Add 
2. Subtract 
3. Multiply 
4. Divide 
5. Power 
6. Factorial 
7. Square Root 
8. Percentage 
9. Show History
10. Exit"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def factorization(a):
    if a >= 0:
        return factorial(a)
    else:  return "Undefined"

def square_root(a):
    if a >= 0:
        return sqrt(a)
    else: return "Undefined"

def percent(a):
    return a / 100

def save_to_history(history):
    with open("operations_history.txt", "a") as file:
        for operation in history:
            file.write(f"{operation}\n")

def show_history():
    try:
        with open("operations_history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["No history available.\n"]

def calculator():
    global result
    operation_history = []
    print(menu())

    while True:
        try:
            decision = int(input("Choose Operator: "))
        except ValueError:
            print("Invalid input. Please choose a valid operation.")
            continue

        if decision == 10:
            print("----Exiting calculator----")
            break

        if decision == 9:
            print("History:")
            for entry in show_history():
                print(entry, end="")
            continue

        if decision in list(range(1, 9)):
            try:
                num1 = float(input("Enter the first number: "))
                if decision in [1, 2, 3, 4, 5]:
                    num2 = float(input("Enter the second number: "))

                if decision == 1:
                    result = add(num1, num2)
                    operation_history.append(f"{num1} + {num2} = {result}")
                elif decision == 2:
                    result = subtract(num1, num2)
                    operation_history.append(f"{num1} - {num2} = {result}")
                elif decision == 3:
                    result = multiply(num1, num2)
                    operation_history.append(f"{num1} * {num2} = {result}")
                elif decision == 4:
                    result = divide(num1, num2)
                    operation_history.append(f"{num1} / {num2} = {result}")
                elif decision == 5:
                    result = power(num1, num2)
                    operation_history.append(f"{num1}^{num2} = {result}")
                elif decision == 6:
                    result = factorization(int(num1))
                    operation_history.append(f"{num1}! = {result}")
                elif decision == 7:
                    result = square_root(num1)
                    operation_history.append(f"sqrt({num1}) = {result}")
                elif decision == 8:
                    result = percent(num1)
                    operation_history.append(f"{num1}% = {result}")
                print(f"Answer: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please choose a valid operation.")

        save_to_history(operation_history)

calculator()

# Guess the Number

import random
def Instructions():
    return ("\nLet's start Guessing...\n"
            "----Instructions---\n"
           "> Enter the range of numbers you want the target number to be between\n"
           "> Enter your guess\n"
           "> See if your guess is too high or too low\n"
           "> Change your guess\n"
           "> The app will tell you when you are right, and how many guesses you had\n"
           "Good Luck!\n")

def Guess_Number(show_instructions=True):
    if show_instructions:
        print(Instructions())

    try:
        user_range = input("Enter the range: ")
        range_split = user_range.split()
        if len(range_split) != 2:
            print("Please enter the range correctly. Start and End seperated by space\n")
            return Guess_Number(show_instructions=False)

        start, end = int(range_split[0]), int(range_split[1])
        if start > end:
            print("The start of the range should be less than the end.\n")
            return Guess_Number(show_instructions=False)

        target = random.randint(start, end)

        attempt = 0

        while True:
            try:
                num = int(input("Enter your guess: "))
                attempt += 1

                while num > target:
                    print("Your guess is too high")
                    num = int(input("Change your guess: "))
                    attempt += 1
                while num < target:
                    print("Your guess is too low")
                    num = int(input("Change your guess: "))
                    attempt += 1
                if num == target:
                    print(f"You are right! You had {attempt} guesses")
                    ans = input("Do you want to play again? Yes/No   \n")
                    if ans.lower() == "yes":
                        return Guess_Number(show_instructions=False)
                    else:
                        break
            except ValueError:
                print("Please enter a number")
    except (ValueError, TypeError):
        print("Please enter the range correctly. Start and End separated by space")
        return Guess_Number(show_instructions=False)

Guess_Number()

