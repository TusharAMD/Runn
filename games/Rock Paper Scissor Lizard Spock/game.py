import random
import simplegui
def nrtona(number):
   

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock" 
    elif number == 2:
        return "paper" 
    elif number == 3:
        return "lizard" 
    elif number == 4:
        return "scissors" 
    else:
        print "Error: Not a valid number" 
    


def natonr(name):
    

    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Error: Not a valid name" 



def rpsls(player_choice): 
    
    print "------------"
    print "------------"    
    
    print "Player chooses " + player_choice 
    
    player_number = name_to_number(player_choice)
    
	comp_number = random.randrange(0,5)
    
    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses " + comp_choice 
    
    diff = (comp_number - player_number) % 5

    if diff == 1 or diff == 2:
        print "Computer Wins"
    elif diff == 3 or diff == 4:
        print "Player Wins"
    else:
        print "Player and computer tie!"
 

#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------    
#----------------------------------------------------------    
    
	
# Event Handlers

def get_input(inp):
	
	if (inp == "rock" or inp == "paper" or inp == "lizard" or 
			inp == "Spock" or inp == "scissors"):		
		rpsls(inp)
	else:
		print "Error: Invalid Input"
	
	


# Creating a Frame

frame = simplegui.create_frame("Rock-paper-scissors-lizard-Spock",200,200)

# Registering Handlers

frame.add_input("Enter your choice: ", get_input,200)	
	
	
# Starting the Frame

frame.start()	
    

	
