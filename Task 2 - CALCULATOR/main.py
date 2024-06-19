def get_number(prompt_func, error_func):
    while True:
        try:
            return float(prompt_func())
        except ValueError:
            error_func("Invalid input. Please enter a valid number.")


def get_operation(prompt_func, error_func):
    operations = {
        '1': 'Addition',
        '2': 'Subtraction',
        '3': 'Multiplication',
        '4': 'Division',
        '5': 'Power (Exponentiation)',
        '6': 'Modulus'
    }

    while True:
        operation = prompt_func(operations)
        if operation in operations:
            return operation
        else:
            error_func("Invalid operation choice. Please enter a valid number (1/2/3/4/5/6).")


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


def calculator(prompt_number_func, prompt_operation_func, display_result_func, error_func, continue_func):
    while True:
        num1 = get_number(prompt_number_func, error_func)
        num2 = get_number(prompt_number_func, error_func)
        operation = get_operation(prompt_operation_func, error_func)
        result = perform_calculation(num1, num2, operation)

        display_result_func(result)

        if not continue_func():
            break


# Example of how the functions can be used with a console-based UI
if __name__ == "__main__":
    def prompt_number_console():
        return input("Enter a number: ")

    def prompt_operation_console(operations):
        print("\nChoose the operation you want to perform:")
        for key, value in operations.items():
            print(f"{key}: {value}")
        return input("Enter the number corresponding to the operation (1/2/3/4/5/6): ")

    def display_result_console(result):
        print(f"\nThe result of your calculation is: {result}")

    def error_console(message):
        print(message)

    def continue_console():
        return input("\nDo you want to perform another calculation? (y/n): ").strip().lower() == 'y'

    print("Welcome to the Python Calculator!")
    calculator(prompt_number_console, prompt_operation_console, display_result_console, error_console, continue_console)
    print("Thank you for using the Python Calculator. Goodbye!")
