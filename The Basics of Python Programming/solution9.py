def merge(a, b):
    mergeList = list()
    i = 0
    j = 0
    while j <= len(b):

        if j == len(b):
            mergeList.extend(a[i:len(a)])
            return mergeList
        elif i == len(a):
            mergeList.extend(b[j:len(b)])
            return mergeList

        if a[i] < b[j]:
            mergeList.append(a[i])
            i += 1
        elif a[i] > b[j]:
            mergeList.append(b[j])
            j += 1
        else:
            mergeList.append(a[i])
            mergeList.append(b[j])
            i += 1
            j += 1


myList_1 = list(map(int, input().split()))
myList_2 = list(map(int, input().split()))

if len(myList_1) > len(myList_2):
    print(*merge(myList_1, myList_2))
else:
    print(*merge(myList_2, myList_1))
