# Debugging

# 1) Use linting to avoid unnecessary errors
# 2) Use IDE or editors ( especially IDE)
# 3) Learn to read the error messages
# 4) Use pdb to debug the code

import pdb


def add(num1, num2):
    # pdb.set_trace()
    return num1 + num2


print(add(4, 5))
