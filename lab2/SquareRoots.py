import copy
import numpy as np


class SquareRoots:

    a = np.zeros((10, 10))
    u = np.zeros((10, 10))
    ut = np.zeros((10, 10))

    # def __init__(self, array):
    #     self.set_u(array)
    #     self.a = array
    #     self.ut = self.get_ut()

    @classmethod
    def solve(cls, mat_a, mat_b):

        cls.set_u(mat_a)
        cls.a = mat_a
        cls.ut = cls.get_ut()

        _ut = copy.deepcopy(cls.ut)
        _u = copy.deepcopy(cls.u)
        b = copy.deepcopy(mat_b)
        y = [0] * len(_u)
        x = [0] * len(_u)
        for i in range(len(_u)):
            m = 0
            for k in range(i):
                m = m + _ut[i][k] * y[k]
            y[i] = (b[i] - m) / _ut[i][i]
        for i in range(len(_u) - 1, -1, -1):
            m = 0
            for k in range(i + 1, len(_u)):
                m = m + _u[i][k] * x[k]
            x[i] = (y[i] - m) / _u[i][i]
        return x

    @classmethod
    def set_u(cls, array):
        u = np.zeros((10, 10))
        a = copy.deepcopy(array)
        for i in range(len(a)):
            for j in range(len(a)):
                s = 0
                if i == j:
                    for k in range(i):
                        s += u[k][i] ** 2
                    u[i][i] = np.sqrt(a[i][i] - s)
                if i < j:
                    for k in range(i):
                        s += u[k][i] * u[k][j]

                    u[i][j] = (a[i][j] - s) / u[i][i]
                if i > j:
                    u[i][j] = 0
        cls.u = copy.deepcopy(u)

    @classmethod
    def get_ut(cls):
        return np.array(cls.u).transpose()


    @classmethod
    def get_determinant(cls):
        det = 1
        for i in range(len(cls.u)):
            det = det * cls.u[i][i]
        det = pow(det, 2)
        return det

    @classmethod
    def get_reverse(cls):
        reverse = []
        for i in range(len(cls.u)):
            reverse.append([0] * len(cls.u))

        for i in range(len(cls.u) - 1, -1, -1):
            for j in range(len(cls.u) - 1, -1, -1):
                if i < j:
                    m = 0
                    for k in range(i + 1, len(cls.u)):
                        m = m + reverse[k][j] * cls.u[i][k]
                    reverse[i][j] = - m
                elif i == j:
                    m = 0
                    for k in range(j + 1, len(cls.u)):
                        m = m + reverse[i][k] * cls.ut[k][j]
                    reverse[i][j] = (1 - m) / cls.ut[j][j]
                elif i > j:
                    m = 0
                    for k in range(j + 1, len(cls.u)):
                        m = m + reverse[i][k] * cls.ut[k][j]
                    reverse[i][j] = -m / cls.ut[j][j]

        return reverse
