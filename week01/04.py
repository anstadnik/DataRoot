class Conv:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    def to_roman(self, n):
        '''
        :param self:
        :param n: int
        :return: str
        '''
        ret = ""
        for i, v in enumerate(self.val):
            while n >= int(v):
                print(n)
                n -= int(v)
                ret += self.syb[i]
        return ret


# TODO:
# finish
print(Conv().to_roman(44))
