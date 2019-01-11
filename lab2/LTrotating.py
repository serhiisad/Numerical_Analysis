import numpy as np
from math import *
from matrix_utils import *

#СЛАР 1
#7. метод LT-обертань

class LTRotation:

    __mat_a = []
    __mat_b = []
    __m_size = 0
    __t_matrices = []
    __a_matrices = []
    __c_cur = 0
    __s_cur = 0
    __mat_l = []
    __vec_y = []
    __vec_x = []


    @classmethod
    def _set_matrices(cls, a, b):
        cls.__mat_a = a
        cls.__mat_b = b
        cls.__m_size = len(a)

        cls.__mat_l = np.zeros((cls.__m_size, cls.__m_size))

        cls.__vec_y = np.zeros((cls.__m_size, 1))
        cls.__vec_x = np.zeros((cls.__m_size, 1))

    @classmethod
    def __get_c(cls, i, j):
        return (cls.__a_matrices[i-1])[i][i] / sqrt((cls.__a_matrices[i-1])[i][i] ** 2 +
                                                    (cls.__a_matrices[i-1])[i][j] ** 2)

    @classmethod
    def __get_s(cls, i, j):
        return (cls.__a_matrices[i-1])[i][j] / sqrt((cls.__a_matrices[i-1])[i][i] ** 2 +
                                                     (cls.__a_matrices[i-1])[i][j] ** 2)

    @classmethod
    def __set_t(cls, i, j):

        t = np.identity(cls.__m_size)
        t[i][i] = cls.__c_cur
        t[j][j] = cls.__c_cur

        t[i][j] = - cls.__s_cur
        t[j][i] = cls.__s_cur

        return t

    @classmethod
    def __set_y(cls):
        for k in range(0, cls.__m_size):
            _sum = 0
            for j in range(0, k):
                _sum += cls.__mat_l[k][j] * cls.__vec_y[j]
            cls.__vec_y[k] = (cls.__mat_b[k] - _sum) / cls.__mat_l[k][k]
        return cls.__vec_y

    @classmethod
    def __get_t_transposed(cls):

        transposed = np.identity(cls.__m_size)
        for mat in cls.__t_matrices:
            transposed = np.dot(mat, transposed)

        return transposed

    @classmethod
    def solve(cls, a, b):

        cls._set_matrices(a, b)

        print("MATRIX A: \n" + matrixToString(cls.__mat_a))
        print("MATRIX B: \n" + matrixToString(cls.__mat_b))

        cls.__a_matrices.append(a)

        for i in range(0, cls.__m_size):
            for j in range(i+1, cls.__m_size):

                # c_i_j and s_i_j calculation

                cls.__c_cur = cls.__get_c(i, j)
                cls.__s_cur = cls.__get_s(i, j)

                print(f"(c{(i, j)}, s{(i, j)}) = " + str((cls.__c_cur, cls.__s_cur)))

                # T matrix calculation
                t_next = cls.__set_t(i, j)
                cls.__t_matrices.append(t_next)

                print(f"T_{(i, j)} = \n" + matrixToString(t_next))
               # A matrix calculation
                a_next = np.dot(cls.__a_matrices[-1], cls.__t_matrices[-1])
                cls.__a_matrices.append(a_next)

        cls.__mat_l = cls.__a_matrices[-1]

        print("MATRIX L: \n" + matrixToString(cls.__mat_l))

        #finding Y-s
        cls.__set_y()

        t_transposed = cls.__get_t_transposed()

        # got the result
        cls.__vec_x = np.dot(t_transposed, cls.__vec_y)

        return cls.__vec_x





