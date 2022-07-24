# Generator is an iterable used to save more memory
# Generators are more performance than lists and save memory so they are faster
def generator_function(num):
    for i in range(num):
        yield i * 2


# Yield method used to move to the next iteration in a generator

g = generator_function(100)
next(g)
next(g)
print(next(g))

# for item in generator_function(1000):
#     print(item)
