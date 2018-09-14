from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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

    def __add__(self, other):
        if self.size() == other.size():
            result = [[] for i in range(len(self.list))]
            for row in range(len(self.list)):
                for element in range(len(self.list[row])):
                    result[row].append(self.list[row][element] +
                                       other.list[row][element])
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = [[] for i in range(len(self.list))]
        for row in range(len(self.list)):
            for element in range(len(self.list[row])):
                result[row].append(self.list[row][element] *
                                   other)
        return Matrix(result)

    __rmul__ = __mul__

    def size(self):
        return tuple((len(self.list), len(self.list[0])))

    def transpose(self):
        lenFirstSelf = len(self.list)
        for row in range(len(self.list[0])):
            res = []
            for element in range(lenFirstSelf):
                res.append(self.list[element][row])
            self.list.append(res)
        for i in range(lenFirstSelf):
            self.list.pop(0)
        return self

    @staticmethod
    def transposed(matrix):
        result = []
        lenFirstSelf = len(matrix.list)
        for row in range(len(matrix.list[0])):
            res = []
            for element in range(lenFirstSelf):
                res.append(matrix.list[element][row])
            result.append(res)
        return Matrix(result)


exec(stdin.read())
