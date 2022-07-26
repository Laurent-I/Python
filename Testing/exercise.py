# from random import randint
#
#
# def run_guess(guess, answer):
#     if 1 < guess < 11:
#         if guess == answer:
#             print('You guessed the number!!!')
#             return True
#     else:
#         print('Input a number 1 to 10')
#         return False
#
#
# if __name__ == '__main__':
#     answer = randint(1, 10)
#     while True:
#         try:
#             guess = int(input('Guess a number 1 to 10:  '))
#             if run_guess(guess, answer):
#                 break
#         except ValueError:
#             print('Please enter a number')
#             continue
