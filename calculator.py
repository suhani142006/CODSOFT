import math

# Initialize empty history list
history = []

# Function to display the operation menu
def show_menu():
    print("\nChoose an operation:")
    print(" + : Addition")
    print(" - : Subtraction")
    print(" * : Multiplication")
    print(" / : Division")
    print(" ^ : Power (num1 ^ num2)")
    print(" % : Remainder")
    print(" √ : Square root (of first number)")
    print(" history : Show calculation history")
    print(" clear : Clear calculation history")
    print(" exit : To quit")

# Main calculator logic
while True:
    show_menu()
    operation = input("Enter the operation: ").strip()

    if operation == 'exit':
        print("Thanks for using the calculator. Goodbye!")
        break

    elif operation == 'history':
        if history:
            print("\n--- Calculation History ---")
            for entry in history:
                print(entry)
        else:
            print("\nHistory is empty.")
        continue

    elif operation == 'clear':
        history.clear()
        print("History cleared.")
        continue

    elif operation == '√':
        num = float(input("Enter the number: "))
        if num >= 0:
            result = math.sqrt(num)
            output = f"√{num} = {result}"
            print(output)
            history.append(output)
        else:
            print("Error: Cannot find square root of negative number!")
        continue

    # Get two numbers for all other operations
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Perform the selected operation
    if operation == '+':
        result = num1 + num2
        output = f"{num1} + {num2} = {result}"
    elif operation == '-':
        result = num1 - num2
        output = f"{num1} - {num2} = {result}"
    elif operation == '*':
        result = num1 * num2
        output = f"{num1} * {num2} = {result}"
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            output = f"{num1} / {num2} = {result}"
        else:
            output = "Error: Cannot divide by zero!"
            print(output)
            continue
    elif operation == '^':
        result = math.pow(num1, num2)
        output = f"{num1} ^ {num2} = {result}"
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
            output = f"{num1} % {num2} = {result}"
        else:
            output = "Error: Cannot take remainder with zero!"
            print(output)
            continue
    else:
        print("Invalid operation. Please try again.")
        continue

    print(output)
    history.append(output)
