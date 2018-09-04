from collections import namedtuple

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

participant = namedtuple('participant', ['exam1',
                                         'exam2',
                                         'exam3',
                                         'sum'])
countPlace = int(inFile.readline())
approve = []

for line in inFile:
    student = participant(*map(int, line.split()[-3:]),
                          sum(map(int, line.split()[-3:])))
    if student.exam1 >= 40 and student.exam2 >= 40 and student.exam3 >= 40:
        approve.append(student.sum)

approve.sort(reverse=True)

countGoodStudents = 0
countBestStudents = 0
boundary = 0
n = countPlace

if len(approve) >= countPlace:
    for point in approve:
        if point >= approve[countPlace - 1]:
            countGoodStudents += 1

for point in approve:
    if point >= approve[0]:
        countBestStudents += 1


if countBestStudents > countPlace:
    boundary = 1
elif countGoodStudents > countPlace:
    while countGoodStudents > countPlace:
        countGoodStudents = 0
        n = approve.index(approve[n - 1]) - 1
        for point in approve:
            if point >= approve[n]:
                countGoodStudents += 1
    boundary = approve[n]
elif len(approve) <= countPlace:
    boundary = 0
else:
    boundary = approve[countPlace - 1]

outFile.writelines(str(boundary))

inFile.close()
outFile.close()
