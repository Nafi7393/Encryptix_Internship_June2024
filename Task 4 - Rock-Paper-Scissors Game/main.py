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


def valid_number_of_games(total_games):
    if total_games % 2 == 1:
        return True
    return False


def main():
    user_score = 0
    computer_score = 0
    total_game_num = int(input("Enter the total number of games to play (must be an odd number): "))
    while not valid_number_of_games(total_game_num):
        print("please put an odd number!")
        total_game_num = int(input("Enter the total number of games to play (must be an odd number): "))

    games_to_win = (total_game_num // 2) + 1

    for game in range(total_game_num):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print("\n--------------------------------")
        print(f" You chose: {user_choice.upper()}")
        print(f" Computer chose: {computer_choice.upper()}")
        print("--------------------------------")

        time.sleep(0.5)  # Adding a slight delay for better readability

        if winner == "tie":
            print(" It's a tie!")
        elif winner == "user":
            print(" You win!")
            user_score += 1
        else:
            print(" You lose!")
            computer_score += 1
        print("--------------------------------\n")

        print(f" Score - YOU: {user_score} | COMPUTER: {computer_score}\n")

        if user_score == games_to_win:
            print("Congratulations! You are the final winner!")
            break
        elif computer_score == games_to_win:
            print("The computer is the final winner. Better luck next time!")
            break

    if user_score != games_to_win and computer_score != games_to_win:
        print("\nThank you for playing! Final score:")
        print(f" YOU: {user_score} | COMPUTER: {computer_score}")


if __name__ == "__main__":
    main()


