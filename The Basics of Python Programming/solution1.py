import math
n = 3.4999999999999999

if 0 < n - math.floor(n) < 0.5:
    rusRound = int(math.floor(n))
else:
    rusRound = int(math.floor(n)) + 1

print(rusRound)
