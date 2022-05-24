from random import randint

start = 1
end = 100
value = randint(start, end)

# print(value)
print("I'm thinking of a number between", start, 'and', end)

guess = None

while guess != value:
    text = input('Guess the number: ')
    guess = int(text)

    if guess < value:
        print('Higher.')
    elif guess > value:
        print('Lower.')

print('Congratulations! You guessed the right answer:', value)
