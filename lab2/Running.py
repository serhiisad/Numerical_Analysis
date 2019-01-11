import copy
from math import *

class Running:

    @staticmethod
    def solve(mat_a, mat_b):
        b = copy.deepcopy(mat_b)
        a = copy.deepcopy(mat_a)
        length = len(a[0])

        el = [0] * length
        delta = [0] * length
        x = [0] * length

        for i in range(length):
            r = b[i]

            if i == 0:
                u = 0
            else:
                u = a[i][i - 1]
            if i == length - 1:
                d = 0
            else:
                d = a[i][i + 1]
            c = a[i][i]
            delta[i] = -d / (c + u * delta[i - 1])
            el[i] = (r - u * el[i - 1]) / (c + u * delta[i - 1])

        x[length-1] = el[length-1]

        for i in range(length - 2, -1, -1):
            x[i] = delta[i] * x[i + 1] + el[i]
        return x


