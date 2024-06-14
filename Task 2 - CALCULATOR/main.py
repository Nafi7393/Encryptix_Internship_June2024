def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    operations = {
        '1': 'Addition',
        '2': 'Subtraction',
        '3': 'Multiplication',
        '4': 'Division',
        '5': 'Power (Exponentiation)',
        '6': 'Modulus'
    }
    print("\nChoose the operation you want to perform:")
    for key, value in operations.items():
        print(f"{key}: {value}")

    while True:
        operation = input("Enter the number corresponding to the operation (1/2/3/4/5/6): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation choice. Please enter a valid number (1/2/3/4/5/6).")


def perform_calculation(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '5':
        return num1 ** num2
    elif operation == '6':
        return num1 % num2


def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()
        result = perform_calculation(num1, num2, operation)

        print(f"\nThe result of your calculation is: {result}")

        another_calculation = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if another_calculation != 'y':
            print("Thank you for using the Python Calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
