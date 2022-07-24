# Error Handling
while True:
    try:
        age = int(input('What is your age \n'))
        var = 10 / age
        raise ValueError('Hey cut it out bro!')
    except ValueError:
        print('Please enter a valid age Number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than zero.')
        break
    else:
        print('Thank you mate!')
        break
    finally:
        print('Okay! I\'m done!')

    print('Can you hear me?')


# def sum_two(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'{err}')
#
#
# print(sum_two('1', 2))
