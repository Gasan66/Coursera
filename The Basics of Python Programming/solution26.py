from sys import stdin
import copy


class Matrix:
    def __init__(self, mlist):
        self.list = copy.deepcopy(mlist)

    def __str__(self):
        res = str()
        for myList in self.list:
            for element in myList:
                res += str(element) + '\t'
            res = res.rstrip()
            res += '\n'
        return res.rstrip()

    def size(self):
        return tuple((len(self.list), len(self.list[0])))


exec(stdin.read())
