# Implementation of our own for loop using the iter and next functions.
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

# Use the StopIteration to handle exceptions


special_for([1, 2, 3, 4, 6, 7, 8, 9, 0])
