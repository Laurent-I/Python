my_file = open('test.txt')

# Reading from the file
print(my_file.readline())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readlines())

my_file.close()

# New Method and a good way without closing

# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write('Whatsapp, man!!!')
#     print(text)
#
# # Appending to a file
# with open('test.txt', mode='a+') as my_file:
#     text = my_file.write(' :)')
#     print(text)
#
# # Creating a new file with write
# with open('app/sad.txt', mode='w') as my_file:
#     text = my_file.write(' :(')
#     print(text)

# File Paths
# with open('app/sad.txt', mode='r') as my_file:
#     print(my_file.read())
