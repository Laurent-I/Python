# Error Handling
# while True:
#     try:
#         age = int(input('What is your age \n'))
#         print(age)
#     except ValueError:
#         print('Please enter a valid age Number')
#     except ZeroDivisionError:
#         print('Please enter age higher than zero.')
#     else:
#         print('Thank you mate!')
#         break

def sum_two(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'{err}')


print(sum_two('1', 2))
