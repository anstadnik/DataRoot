def prime_nums(n):
    '''
    :param n: int
    :return: list[int]
    '''
    sieve = [True for i in range(n)]
    ret = []
    print(sieve)
    for i, p in enumerate(sieve):
        if i > 1:
            if p:
                ret.append(i)
                num = i
                while num < n:
                    print(num)
                    sieve[num] = False
                    num += i
        print("hehey")
    return ret


print(prime_nums(30))
