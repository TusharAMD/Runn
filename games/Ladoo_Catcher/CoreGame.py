import random

def ladoo_catcher_game():
    print("Welcome to Ladoo Catcher Game!")
    print("Use 'a' to move left, 'd' to move right, and 'q' to quit.")

    basket_position = 5
    points = 0

    while True:
        ladoo_position = random.randint(1, 10)

        # Display the game state
        print("\n" + "-" * 15)
        print(" " * (basket_position - 1) + "[O]" + " " * (10 - basket_position))
        print("-" * 15)
        print(" " * (ladoo_position - 1) + "L" + " " * (10 - ladoo_position))

        action = input("Move left (a), move right (d), or quit (q): ").lower()

        if action == 'a':
            basket_position = max(1, basket_position - 1)
        elif action == 'd':
            basket_position = min(10, basket_position + 1)
        elif action == 'q':
            print("Game over! You scored {} points.".format(points))
            break
        else:
            print("Invalid input. Use 'a' to move left, 'd' to move right, and 'q' to quit.")

        # Check if the ladoo is caught
        if ladoo_position == basket_position:
            points += 1
            print("Ladoo caught! Points: {}".format(points))

if __name__ == "__main__":
    ladoo_catcher_game()
