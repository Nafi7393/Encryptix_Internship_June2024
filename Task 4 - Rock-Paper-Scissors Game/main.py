import random
import time


def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Choose ROCK, PAPER, or SCISSORS: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose ROCK, PAPER, or SCISSORS.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


def display_result(user_choice, computer_choice, winner):
    print("\n--------------------------------")
    print(f" You chose: {user_choice.upper()}")
    print(f" Computer chose: {computer_choice.upper()}")
    print("--------------------------------")

    time.sleep(0.5)  # Adding a slight delay for better readability

    if winner == "tie":
        print(" It's a tie!")
    elif winner == "user":
        print(" You win!")
    else:
        print(" You lose!")
    print("--------------------------------\n")


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f" Score - YOU: {user_score} | COMPUTER: {computer_score}\n")

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("\nThank you for playing! Final score:")
            print(f" YOU: {user_score} | COMPUTER: {computer_score}")
            break


if __name__ == "__main__":
    main()
