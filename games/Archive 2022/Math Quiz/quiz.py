from time import time
from random import randint

while True:
    num1 = randint(5, 9)
    num2 = randint(2, 3)
    product = num1 * num2
    start_time = time()
    response = int(input(f'What is {num1} * {num2}? '))
    elapsed_time = time() - start_time
    if not response:
        break
    try:
        solution = int(response)
        print(f'Correct, in {elapsed_time}' if solution == product else 'Wrong' )
    except ValueError:
        print('Wrong Answer')