def CountSort(myList):

    sort = [0] * (max(myList) + 1)

    for num in myList:
        sort[num] += 1
    resList = []
    for i in range(len(sort)):
        for j in range(sort[i]):
            resList.append(i)
    return list(map(int, resList))


inList = list(map(int, input().split()))
print(*CountSort(inList))
