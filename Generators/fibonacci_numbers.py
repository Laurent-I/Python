# Using Generators to create the fibonacci numbers sequence generator
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(100):
    print(x)


# Using List to create the fibonacci numbers sequence generator
# def fib2(number):
#     a = 0
#     b = 1
#     result = []
#     for i in range(number):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result
#
#
# print(fib2(20))
# print(__name__)