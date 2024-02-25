words = input().split()
for word in words:
    if word.lower() == word[::-1].lower():
        print(word)