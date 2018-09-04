from collections import namedtuple

participant = namedtuple('participant', ['surname',
                                         'point'])

print(participant(*input().split()))
