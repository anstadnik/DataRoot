import numpy as np
def nearest_to_scalar(matrix, n):
    '''
    :param matrix: numpy.ndarray[list[list[int]]]
    :param n: int
    :return: int
    '''
    # print(list([[abs(i - n)] for i in l] for l in matrix))
    print([[[abs(i - n)] for i in l] for l in matrix])
    return np.min([[[abs(i - n)] for i in l] for l in matrix])

print(nearest_to_scalar(np.array([[1, 2, 3], [3, 4, 5]]), 3.4))
