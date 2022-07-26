import re

# At least 8 Characters long
# Contains any sort of letters, numbers $%#@

pattern = re.compile(r'[a-zA-Z\d$%#@]{8,}\d')
password = 'hfbhfbd223fc$$%6@78'

check = pattern.fullmatch(password)
print(check)
