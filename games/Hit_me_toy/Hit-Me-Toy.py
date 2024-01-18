import random

def hit_me_toy():
    print("Welcome to Hit Me Toy!")
    print("I have selected a random number between 1 and 100. Your task is to guess it.")

    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    hit_me_toy()
