import random
import string


def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    # Base character set: always include lowercase letters
    char_set = string.ascii_lowercase

    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    # Ensure that the password has at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from the character set
    password += [random.choice(char_set) for _ in range(length - len(password))]

    # Shuffle the list to ensure randomness and convert it to a string
    random.shuffle(password)
    return ''.join(password)


def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length must be greater than 0.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")


if __name__ == "__main__":
    main()
