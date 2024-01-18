import random

def hit_me_toy_game():
    print("Welcome to Hit Me Toy Game!")

    total_points = 0
    attempts = 0

    while True:
        input("Press Enter to punch the toy...")
        
        # Generate a random strength for the toy
        toy_strength = random.randint(1, 10)

        # Get the player's punch strength (assuming a valid input)
        punch_strength = int(input("Enter the strength of your punch (1-10): "))
        
        # Calculate points based on the difference between toy and punch strength
        points = max(0, 10 - abs(toy_strength - punch_strength))
        total_points += points

        print(f"Toy strength: {toy_strength}")
        print(f"You scored {points} points!")

        play_again = input("Do you want to punch again? (yes/no): ").lower()
        attempts += 1

        if play_again != 'yes':
            break

    print(f"Game over! You scored a total of {total_points} points in {attempts} attempts.")

if __name__ == "__main__":
    hit_me_toy_game()
