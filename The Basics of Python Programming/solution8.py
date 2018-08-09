rangeList = int(input())
myList = list(map(int, input().split()))
x = int(input())

if x >= myList[0]:
    difference = x - myList[0]
else:
    difference = myList[0] - x

for i in myList:
    if x >= i:
        if x - i <= difference:
            near = i
            difference = x - i
    else:
        if i - x <= difference:
            near = i
            difference = i - x
print(near)
