def str_to_dict(some_str):
    '''
    :param some_str: str
    :return: dict
    '''
    a = {}
    for i in some_str:
        if i not in a:
            a[i] = 0
        a[i] += 1
    print(a)
    return a


print(str_to_dict('dataroot_university'))
