# zip

my_list = [1, 2, 3]
your_list = [10, 20, 30]
theirs = (4, 5, 6)


def only_odd(item):
    return item % 2 != 0


print((list(zip(my_list, your_list, theirs))))
print(my_list)
