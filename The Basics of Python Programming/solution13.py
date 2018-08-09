myList = list(map(int, input().split()))

for i in myList:
    if i > 0:
        value = i
        break

for i in myList:
    if value > i > 0:
        value = i
print(value)
