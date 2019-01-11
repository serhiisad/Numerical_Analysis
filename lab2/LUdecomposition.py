import numpy as np
from matrix_utils import *
import copy

#СЛАР 1
#3. LU-факторизація з наявною одиничною діагоналлю у матриці U

class LUdecomposition:

    #2darray
    __mat_a = []
    #1darray
    __mat_b = []
    __m_size = 0
    __mat_l = []
    __mat_u = []
    __vec_y = []
    __vec_x = []

    # def __init__(self, a, b):
    #     self.mat_a = np.array(a)
    #     self.mat_b = np.array(b)
    #
    #     self.m_size = len(a)
    #
    #     self.mat_l = np.zeros((self.m_size, self.m_size))
    #     self.mat_u = np.identity((self.m_size))
    #     self.vec_y = np.zeros((self.m_size, 1))
    #     self.vec_x = np.zeros((self.m_size, 1))

    @classmethod
    def _set_matrices(cls, a, b):
        cls.__mat_a = a
        cls.__mat_b = b

        cls.__m_size = len(a)

        cls.__mat_l = np.zeros((cls.__m_size, cls.__m_size))

        # наявна одинична діагональ в матриці U
        cls.__mat_u = np.identity(cls.__m_size)

        cls.__vec_y = np.zeros((cls.__m_size, 1))
        cls.__vec_x = np.zeros((cls.__m_size, 1))

    @classmethod
    def __l_ij(cls, i, j):
        _sum = 0
        for k in range(0, j):
            _sum += (cls.__mat_u[k][j] * cls.__mat_l[i][k])
        return cls.__mat_a[i][j] - _sum

    @classmethod
    def __u_ij(cls, i, j):
        _sum = 0
        for k in range(0, i):
            _sum += (cls.__mat_u[k][j] * cls.__mat_l[i][k])
        return (cls.__mat_a[i][j] - _sum) / cls.__mat_l[i][i]

    @classmethod
    def __y_i(cls, i):
        b_i = cls.__mat_b[i]
        _sum = 0
        for k in range(0, i):
            _sum += cls.__mat_l[i][k] * cls.__vec_y[k]
        return (b_i - _sum)/cls.__mat_l[i][i]

    @classmethod
    def __x_i(cls,  i):
        _sum = 0
        for k in range(i, cls.__m_size):
            _sum += cls.__mat_u[i][k] * cls.__vec_x[k]
        return cls.__vec_y[i] - _sum

    @classmethod
    def __lu_factorize(cls):
        for i in range(0, cls.__m_size):
            for j in range(0, cls.__m_size):
                if i >= j:
                    cls.__mat_l[i][j] = cls.__l_ij(i, j)
                else:
                    cls.__mat_u[i][j] = cls.__u_ij(i, j)

            # print("matrix L: \n" + matrixToString(cls.__mat_l))
            # print("matrix U: \n" + matrixToString(cls.__mat_u))

    @classmethod
    def solve(cls, a, b):

        cls._set_matrices(a, b)

        cls.__lu_factorize()
        print("Matrix A:\n" + matrixToString(cls.__mat_a) + "\n")
        print("Matrix B:\n" + matrixToString(cls.__mat_b) + "\n")
        print("Matrix L:\n" + matrixToString(cls.__mat_l) + "\n")
        print("Matrix U:\n" + matrixToString(cls.__mat_u) + "\n")

        for i in range(0, cls.__m_size):
            cls.__vec_y[i] = cls.__y_i(i)
        for i in reversed(range(0, cls.__m_size)):
            cls.__vec_x[i] = cls.__x_i(i)

        print("Y_i:\n" + matrixToString(cls.__vec_y))
        print("X_i:\n" + matrixToString(cls.__vec_x))

        return cls.__vec_x


    @classmethod
    def get_determinant(cls):
        det = 1
        for i in range(cls.__m_size):
            det *= cls.__mat_l[i][i]
        return det



    @classmethod
    def get_inverse(cls):

        _l = copy.deepcopy(cls.__mat_l)
        _u = copy.deepcopy(cls.__mat_u)
        cls.__m_size = np.shape(_l)[0]
        cls.__lu_factorize()

        _identity = np.identity(cls.__m_size)
        inverse = np.zeros((cls.__m_size, cls.__m_size))

        for i in range(cls.__m_size):

            #solving system L*y = e_i
            y_i = cls.solve(_l, _identity[i])
            # print("Y_i = " + str(y_i))

            #finding x_i
            x_i = cls.solve(_u, np.array(y_i))
            # print("X_i = " + str(x_i))
            # print("\n " + str(inverse))

            inverse[i] = list(x_i.flat)

        # print("inverse matrix" + str(inverse))
        return np.transpose(inverse)




