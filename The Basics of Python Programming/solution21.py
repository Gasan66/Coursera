inFile = open('input.txt', 'r', encoding='utf8')

myDict = {}
for line in inFile:
    for word in line.split():
        myDict[word] = myDict.get(word, 0) + 1

myList = list(myDict.items())
myList.sort(key=lambda x: x[0])
myList.sort(key=lambda x: x[1], reverse=True)

print(myList[0][0])
inFile.close()
