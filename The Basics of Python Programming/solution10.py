freeSpace, countUser = tuple(map(int, input().split()))
k = 0
i = 0
userSpace = list()
sumUserSpace = 0

while k < countUser:
    userSpace.append(int(input()))
    k += 1
userSpace.sort()

for space in userSpace:

    sumUserSpace += space

    if sumUserSpace < freeSpace:
        i += 1
    elif sumUserSpace == freeSpace:
        i += 1
        break

print(i)
