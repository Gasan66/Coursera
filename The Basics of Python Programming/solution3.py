n = int(input())
Seq = n
i = 1
save = 1
while n != 0:
    n = int(input())
    if n == Seq:
        i += 1
    elif i > save:
        save = i
        i = 1
    else:
        i = 1
    Seq = n
print(save)
