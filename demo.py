import random

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    play_again = True

    while play_again:
        input("Press Enter to roll the dice...")

        result = roll_dice()
        print(f"You rolled a {result}!")

        play_again = input("Do you want to roll again? (yes/no): ").lower().startswith('y')

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
