# The built-in collection module

from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7]
# print(Counter(li))

# dictionary = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# print(dictionary['g'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)
