import random

def play_game():
    options = ["Rock", "Paper", "Scissors"]

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user_choice not in options:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(options)

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "Rock" and computer_choice == "Scissors":
            print("You win!")
        elif user_choice == "Paper" and computer_choice == "Rock":
            print("You win!")
        elif user_choice == "Scissors" and computer_choice == "Paper":
            print("You win!")
        else:
            print("Computer wins!")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Run the game
play_game()