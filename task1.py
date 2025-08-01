# calculator.py

# --- Step 1: Define functions for each operation ---
# These are the building blocks of our calculator. Each function takes two numbers and returns the result of the operation. 

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    # We need to handle the case where the user tries to divide by zero
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

# --- Step 2: Create the main loop to run the calculator ---
# This `while True` loop will keep the program running until the user decides to exit. 

while True:
    # --- Step 3: Get user input ---
    # We present the options to the user and take their choice. 
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # The input() function captures what the user types. 
    choice = input("Enter choice(1/2/3/4/5): ")

    # --- Step 4: Check the user's choice and perform the action ---
    # We use conditional statements (if/elif/else) to decide what to do.

    # Check if the user wants to exit
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break # This keyword exits the loop

    # Check if the choice is one of the valid operations
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue # This skips the rest of the loop and starts over

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    
    else:
        # This message is shown if the user enters something other than 1, 2, 3, 4, or 5
        print("Invalid Input. Please enter a valid choice.")