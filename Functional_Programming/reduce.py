# reduce

from functools import reduce

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


print((reduce(accumulator, my_list, 10)))
print(my_list)
