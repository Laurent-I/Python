import re

# Email Regular Expression pattern
pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
string = 'irakramlaw@gmail.com'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
print(b)
print(c)
print(a.span())
print(a.start())
print(a.end())
print(a)
