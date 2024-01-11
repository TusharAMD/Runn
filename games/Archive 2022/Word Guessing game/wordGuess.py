import random

words = ["lemon","mango","banana","apple"]

name=input("Enter  Your name")
print(f"Hi {name} , Let's start the game")

print("\n\n\n\t\t ***Word Guessing Game*** ")
print("\n You have 10 attempts to guess the word correctly .")

wrong_list=[]

original_word=random.choice(words)
print(f"The word is of {len(original_word)} letters. ")

guessed_word = []
for i in range(len(original_word)):
    guessed_word.append("__")
print(*([i for i in guessed_word]))
c=8
while(c):
    c=c-1 
    
    guessed_letter = input("Guess the  letter")
   
    if not guessed_letter.isalpha():
        print('Guess only a letter')
    
    elif(len(guessed_letter)>1):
        print('Guess only one letter...')
    
    elif(guessed_letter in wrong_list):
        print('You have Already guessed this letter')
   
    if guessed_letter in original_word:
        for i in range(len(original_word)):
            if original_word[i] == guessed_letter:
                guessed_word[i]=original_word[i] 
    else:
        """if guessed_letter is not in original_word 
           prompt user for wrong chosen letter"""
        print("You Guessed wrong letter")
        wrong_list.append(guessed_letter)
    guess_word = [i for i in guessed_word]
    guess_word = "".join(guess_word)
    if original_word ==guess_word :
        print('YAY !!, You have Got the letter ...')
        exit(0)
    
    print(*([i for i in guessed_word]))
  
    print(f"You have {c} attempts left")
    if c==0:
        if  original_word!=guessed_word  :
            print(f"You lost the game ,The original Word was {original_word}")
            exit(0)
