x, y = float(input()), int(input())
i = 1
if x != y:
    while x < y:
        x = x + x * 0.1
        i += 1
    print(i)
elif x == y == 0:
    print(0)
else:
    print(i)
