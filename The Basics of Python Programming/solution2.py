def sum(a, b):
    if b > 0:
        b -= 1
        a += 1
        return sum(a, b)
    return a


x, y = int(input()), int(input())
print(sum(x, y))
