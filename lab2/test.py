# mat = read_matrix('task1/a.txt')
# print(matrixToString(mat) + "\n")
from matrix_utils import *
from Running import Running
from SquareRoots import SquareRoots
from LUdecomposition import LUdecomposition
from LTrotating import LTRotation
import time


print("................................TASK1..................................\n")
#
# mat_a = np.array([[3, -1, 0], [-2, 1, 1], [2, -1, 4]])
# mat_b = np.array([5, 0, 15])

mat_a = np.array([[2, 1, 1], [1, -1, 0], [3, -1, 2]])
mat_b = np.array([2, -2, 2])

# mat_a = read_matrix('task1/a.txt')
# mat_b = read_matrix('task1/b.txt')
#
print("LU_decomposition RESULT:\n\n" + str(LUdecomposition.solve(mat_a, mat_b)) + "\n\n")
#
# print("det A = " + str(LUdecomposition.get_determinant()) + "\n")

print("A_-1: \n" + matrixToString(LUdecomposition.get_inverse()) + "\n")

# print("LT_rotation RESULT:\n\n" + str(LTRotation.solve(mat_a, mat_b)) + "\n\n")

print("_____________________________________________________________________\n")


print("................................TASK2..................................\n")

# mat_a = read_matrix('task2/a.txt')
# print(matrixToString(mat_a))
# mat_b = read_matrix('task2/b.txt')
# print(matrixToString(mat_b))
#
# print("SQUARE ROOTS RESULT:\n\n" + matrixToString(SquareRoots.solve(mat_a, mat_b)) + "\n\n")
#
# print("A_-1 = \n" + matrixToString(SquareRoots.get_reverse()))



print("_____________________________________________________________________\n")


print("................................TASK3..................................\n")

# mat_a = read_matrix('task3/a.txt')
# print(matrixToString(mat_a))
# mat_b = read_matrix('task3/b.txt')
# print(matrixToString(mat_b))
#
# start_time = time.time()
# print("RUNNING RESULT:\n\n" + matrixToString(Running.solve(mat_a, mat_b)) + "\n\n")
# print(f"time = {time.time() - start_time}")
#
# start_time1 = time.time()
# print("LU RESULT:\n\n" + matrixToString(LUdecomposition.solve(mat_a, mat_b)) + "\n\n")
# print(f"time = {time.time() - start_time1}")

print("_____________________________________________________________________\n")
