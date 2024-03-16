password = input()
low = False
up = False
digit = False
for elem in password:
    if elem.isupper():
        up = True
    elif elem.islower():
        low = True
    if elem.isdigit():
        digit = True
if up == True and low == True and digit == True and len(password) >= 8:
    print('Yes')
else:
    print('No')