from collections import namedtuple
n = int(input())

participant = namedtuple('participant', ['surname',
                                         'point'])
participants = []

for i in range(n):
    t = input().split()
    participants.append(participant(t[0], int(t[1])))

participants.sort(key=lambda x: x.point, reverse=True)

for member in participants:
    print(member.surname)
