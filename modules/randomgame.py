from random import randint
import sys
# generate a number 1 - 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# input from user?
# check that input is a number 1 to 10
while True:
    try:
        guess = int(input('Guess a number 1 to 10:  '))
        if 1 < guess < 11:
            if guess == answer:
                print('You guessed the number')
                break
        else:
            print('Input a number 1 to 10')
    except ValueError:
        print('Please enter a number')
        continue

# check if the number is the right guess.
# ask again
