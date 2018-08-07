def sumSeq():
    a = int(input())
    if a != 0:
        a += sumSeq()
    return a


print(sumSeq())
