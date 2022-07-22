# Error Handling
while True:
    try:
        age = int(input('What is your age \n'))
        print(age)
    except ValueError:
        print('Please enter a valid age Number')
    except ZeroDivisionError:
        print('Please enter age higher than zero.')
    else:
        print('Thank you mate!')
        break
