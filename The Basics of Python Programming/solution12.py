n = int(input())
villageDistList = list(map(int, input().split()))
m = int(input())
shelterDistList = list(map(int, input().split()))

villageList = list()
shelterList = list()

for village in range(1, n + 1):
    villageList.append((villageDistList[village - 1], village))

villageList.sort()

for shelter in range(1, m + 1):
    shelterList.append((shelterDistList[shelter - 1], shelter))

shelterList.sort()

v = 0
s = 0
nearShelterList = []

while v < n:
    distForShelter = (villageList[v][0] - shelterList[s][0]) ** 2
    distForShelterList = []
    while s < len(shelterList):
        if (villageList[v][0] - shelterList[s][0]) ** 2 <= distForShelter:
            distForShelter = (villageList[v][0] - shelterList[s][0]) ** 2
            distForShelterList.append(
                (distForShelter, shelterList[s][1], villageList[v][1], s)
                                     )
            s += 1
        else:
            break
    distForShelterList.sort()
    nearShelterList.append(
        (distForShelterList[0][2], distForShelterList[0][1])
                          )
    v += 1
    s = distForShelterList[0][3]
nearShelterList.sort()
for shelter in nearShelterList:
    print(shelter[1], end=' ')
