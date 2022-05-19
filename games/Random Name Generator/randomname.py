# Random Name Generator Game
# Made by -  TRIDIB BAG , GSSoC'22 

import random


first = ["joy", "rabi", "jonny", "Ankita", "Suor", "Puchur", "jack", "Riley", "Poltu", "Leo"]


middle = ["Kumar", "Griffith", "Andy", "Singh", "Eva", "Emma", "Olivia", "Sims", "Spon", "Ovilia"]


last = ["Bag", "PAl", "samson", "Jordan", "paul", "Nath", "Singh", "Das", "Sena", "nandy"]


namebank = []



print("                                             Generate Random Name                  ")

while True:


    name = input("Do you want to generate a new name? [y/n]: ")

    if name.upper() == "Y":

        rand = random.randint(0, 4)

        randname = first[rand] + " " + middle[rand] + " " + last[rand]

        namebank.append(randname)

        print(f"Your new name is {randname}\n")

        continue

    elif name.upper() == "N":

        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Thank you!")

        print("\n")

        print("List of generated names:")

        for x in namebank:

            print(f"{x}")
        
        break