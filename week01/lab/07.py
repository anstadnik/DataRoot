import numpy as np


def add_mean_and_calc_det(matrix):
    '''
    :param my_list: numpy.ndarray[list[list[int]]]
    :return: numpy.float64
    '''
    matrix2 = []
    for l in matrix:
        mean = np.average(l)
        matrix2.append([i * mean for i in l])
    print(matrix2)
    return np.linalg.det(matrix2)

