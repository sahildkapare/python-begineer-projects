import random

def numbguess_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    numbto_guess = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10")
                continue

            if guess < numbto_guess:
                print("Too low! Try again.")
            elif guess > numbto_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {numbto_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Simple play again option added at the end
    play_again = input("\nWould you like to play again? (y/n): ")
    if play_again.lower() in ['y', 'yes']:
        numbguess_game()  # Call the function again to restart
    else:
        print("Thanks for playing! Goodbye!")

# Run the game
numbguess_game()
