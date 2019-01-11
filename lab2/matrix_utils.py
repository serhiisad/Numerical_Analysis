import numpy as np

def read_matrix(filepath):
    return np.loadtxt(filepath)

def write_matrix(matrix, filepath):
    np.savetxt(filepath, matrix)

def matrixToString(matrix):
    mat_str = ""
    for row in matrix:
        if not isinstance(row, (np.ndarray, list, tuple,)):
            # mat_str += '{:.3f}'.format(round(row, 3)) + '\t'
            mat_str += str(round(row, 3)) + "\t"
        else:
            for number in row:
                 # mat_str += '{:06.3f}'.format(round(number, 3)) + '\t'
                 mat_str += str(round(number, 3)) + "\t"
        mat_str += '\n'
    return mat_str
    # return np.array2string(matrix, formatter={'float_kind': lambda x: "%7.2f" % x})
