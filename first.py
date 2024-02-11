a = input()
a = a.split()
max = a[0]
for i in range(len(a)):
    if len(max) < len(a[i]):
        max = a[i]
print(max)
print(len(max))