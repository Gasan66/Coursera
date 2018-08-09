# n = int(input())
# villageDistList = list(map(int, input().split()))
# m = int(input())
# shelterDistList = list(map(int, input().split()))
import time
start_time = time.time()

n = 10
villageDistList = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
m = 10
shelterDistList = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]

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
distForShelter = list()

while v < n:
    distForShelter = list()
    for s in range(len(shelterList)):
        distForShelter.append(
            ((villageList[v][0] - shelterList[s][0]) ** 2,
             shelterList[s][1]))
    distForShelter.sort()
    nearShelterList.append((villageList[v][1] - 1, distForShelter[0][1]))
    v += 1
nearShelterList.sort()
for shelter in nearShelterList:
    print(shelter[1], end=' ')

print("--- %s seconds ---" % (time.time() - start_time))
