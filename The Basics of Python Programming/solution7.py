def revSeq():
    a = int(input())
    if a != 0:
        revSeq()
    print(a)


revSeq()
