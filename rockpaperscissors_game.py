import random

def get_user_choice():
    """Prompt the user for their choice and validate it."""
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice! Please try again.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of a single round."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game(round_limit=5):
    """Main game loop with score tracking and round limit."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    print(f"The game will be played for {round_limit} rounds.\n")

    for round_num in range(1, round_limit + 1):
        print(f"--- Round {round_num} ---")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}\n")

    print("=== Game Over ===")
    print(f"Final Score => You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer wins the game. Better luck next time!")
    else:
        print("It's a draw overall!")

# Run the game
play_game(round_limit=5)
