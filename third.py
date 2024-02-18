n = 5
L = 1
a = [1,3,4,10,11,13]
count = 0
i = 0
while i < len(a):
    if i == len(a) - 1:
        count += 1
        break
    elif a[i+1] - a[i] != L:
        count += 1
        i += 1
    else:
        count += 1
        i += 2
print(count)