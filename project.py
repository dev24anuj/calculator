# num1 = float(input("enter first number : " ))
# num2 = float(input("enter second number : ")) 
# sum = (num1 + num2)
# print(f"the sum of {num1} and {num2} is ={sum}")
# total = 0  # Initialize sum
# while True:
#     try:
#         num = float(input("Enter a number (or type '=' to finish): "))
#         total += num  # Add the number to total
#     except ValueError:  # If input is not a number, check if it's 'done'
#         user_input = input("Do you want to stop? Type 'done' to finish: ").strip().lower()
#         if user_input == '=':
#             break  # Exit loop

# print(f"The total sum of entered numbers is: {total}")
def calculator():
    try:
        total = float(input("Enter the first number: "))  # Take the first number
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    while True:
        operation = input("Choose an operation (+, -, *, /) or type 'exit' to stop: ").strip()

        if operation.lower() == 'exit':  # Allow user to exit anytime
            break

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation! Please choose from +, -, *, /")
            continue

        try:
            num = float(input("Enter another number: "))  # Take next number
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Perform the chosen operation
        if operation == '+':
            total += num
        elif operation == '-':
            total -= num
        elif operation == '*':
            total *= num
        elif operation == '/':
            if num == 0:
                print("Division by zero is not allowed. Try again.")
                continue
            total /= num

        print(f"Current result: {total}")  # Show updated result

    print(f"Final result: {total}")  # Display final result when user exits

# Run the calculator
calculator()
