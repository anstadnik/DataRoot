def sec_smallest(numbers):
    '''
    :param numbers: list[int]
    :return: int
    '''
    numbers.remove(min(numbers))
    return min(numbers)


print(sec_smallest([1, 2, -8, -2, 0]))
