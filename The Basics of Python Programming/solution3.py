def power(a, n):
    n -= 1
    if n > 0:
        if n % 2 == 0:
            a *= power(a * a, n / 2)
        else:
            a *= power(a, n)
    return a


x, y = float(input()), float(input())
if y == 0:
    print(1)
elif y % 2 == 0:
    print(power(x * x, y / 2))
else:
    print(power(x, y))
