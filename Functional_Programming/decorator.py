# Decorator: supercharge functions: A Function that wraps another Function and enhances it
# def my_decorator(func):
#     def wrap_func():
#         print('******')
#         func()
#         print('******')
#
#     return wrap_func
#
#
# @my_decorator
# def hello():
#     print('Hello!!!')
#
#
# @my_decorator
# def bye():
#     print('See ya Later!!!')
#
#
# hello()

# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_func


@my_decorator
def hello(greeting, emoji=';)'):
    print(greeting, emoji)


hello('Hiiiiii!!!!!')
