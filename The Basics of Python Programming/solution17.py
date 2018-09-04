n = int(input())
schoolList = []
langSet = set()
minSet = set()
maxSet = set()
for schoolboy in range(n):

    countLang = int(input())
    langSet = set()

    for lang in range(countLang):
        langSet.add(* input().split())

    if schoolboy == 0:
        minSet = langSet
    else:
        minSet &= langSet

    maxSet |= langSet

print(len(minSet))

for i in minSet:
    print(i)

print(len(maxSet))

for i in maxSet:
    print(i)
