import numpy as np


def nearest_to_scalar(matrix, n):
    '''
    :param matrix: numpy.ndarray[list[list[int]]]
    :param n: int
    :return: int
    '''
    array = []
    minimal = -1
    rez = 0
    for l in matrix:
        for num in l:
            if abs(n - num) < minimal or minimal == -1:
                minimal = abs(n - num)
                rez = num
    return rez


print(nearest_to_scalar(np.array([[1, 2, 3], [4, 5, 6]]), 3.4))
