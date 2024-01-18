import random
import time

def display_intro():
    print("Welcome to the Campfire Adventure!")
    print("You find yourself in the woods around a campfire.")
    print("Make choices to navigate through the adventure.")

def make_choice(options):
    print("Choose an option:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ignite_campfire():
    print("You want to ignite the campfire.")
    time_taken = random.uniform(1, 5)  # Simulating time taken to ignite the fire

    if time_taken < 3:
        print("You successfully ignite the campfire by rubbing your hands together!")
        return True
    else:
        print("It takes a bit longer to ignite the campfire.")
        return False

def campfire_scene():
    if ignite_campfire():
        print("You sit by the warm campfire, enjoying the crackling flames.")
        options = ["Roast marshmallows", "Tell a ghost story", "Go to sleep"]
        choice = make_choice(options)

        if choice == 1:
            print("You roast marshmallows and enjoy the sweet treat.")
        elif choice == 2:
            print("You tell a spooky ghost story, making the atmosphere even more thrilling.")
        else:
            print("You go to sleep, feeling cozy and safe around the campfire.")
    else:
        print("You struggle to ignite the campfire, and it remains unlit.")

def encounter_wildlife():
    print("You hear rustling in the bushes nearby.")
    options = ["Investigate", "Ignore"]
    choice = make_choice(options)

    if choice == 1:
        print("You cautiously approach and discover a friendly bunny. It hops away.")
    else:
        print("You decide to ignore it and continue enjoying the campfire.")

def protect_fire():
    print("You notice that the wind is picking up, and there's a chance the fire might go out.")
    options = ["Build a windbreak", "Let it be"]
    choice = make_choice(options)

    if choice == 1:
        print("You build a windbreak using rocks and branches, protecting the campfire from the wind.")
    else:
        print("You decide to let it be and hope the fire continues to burn.")

def main():
    display_intro()

    while True:
        options = ["Sit by the campfire", "Explore the surroundings", "Quit"]
        choice = make_choice(options)

        if choice == 1:
            campfire_scene()
        elif choice == 2:
            encounter_wildlife()
        else:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
