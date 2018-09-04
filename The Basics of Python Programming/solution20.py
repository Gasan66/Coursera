inFile = open('input.txt', 'r', encoding='utf8')

myDict = {}
for line in inFile:
    for word in line.split():
        print(myDict.get(word, 0), end=' ')
        myDict[word] = myDict.get(word, 0) + 1

inFile.close()
