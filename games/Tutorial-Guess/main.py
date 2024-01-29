
import random, sys

LOW_NUMBER = 1
HIGH_NUMBER = 20

secretNumber = random.randint(LOW_NUMBER, HIGH_NUMBER)


print('Hello! What is your name?')
playerName = input()
print('It is good to meet you, ' + playerName)

print('I am thinking of a number from', LOW_NUMBER, 'to', HIGH_NUMBER)
print('You get 6 guesses.')

for i in range(6):
    print('Take a guess, or enter QUIT.')
    guess = input()

    if guess == 'QUIT':
        sys.exit()

    if int(guess) < secretNumber:
        print('Your guess was too low.')
    elif int(guess) > secretNumber:
        print('Your guess was too high.')
    elif int(guess) == secretNumber:
        break

print('My secret number was', secretNumber)
if guess == str(secretNumber):
    print('You guessed my number!')
else:
    print('You did not guess my number. Better luck next time.')