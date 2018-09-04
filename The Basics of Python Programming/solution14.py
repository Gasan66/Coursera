from collections import namedtuple

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

participant = namedtuple('participant', ['surname',
                                         'name',
                                         'schoolnumber',
                                         'point'])
participants = []

for line in inFile:
    participants.append(participant(*line.strip().split()))

participants.sort(key=lambda x: x.surname)
for people in participants:
    outFile.writelines(str(people.surname) + ' ' +
                       str(people.name) + ' ' +
                       str(people.point) + '\n')

inFile.close()
outFile.close()
