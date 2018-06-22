import numpy as np


def svd_ranks(Z):
    '''
    :param Z: numpy.ndarray[list[list[int]]]
    :return: list
    '''
    return list(map(np.linalg.matrix_rank, [*np.linalg.svd(Z)]))


print("hehey")
print(svd_ranks(np.array([[1, 2, 3], [4, 5, 6]])))
