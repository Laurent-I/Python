# lambda expression
# they are Anonymous functions, that only need to run once
# lambda param: action(param)

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


print(list(map(lambda item: item*2, my_list)))
print(my_list)