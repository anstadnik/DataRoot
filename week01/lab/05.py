class MyList:

    def recurse(self, beg, lst, length, tabs):
        print('  ' * tabs, "beg =", beg)
        print('  ' * tabs, "lst =", lst)
        print('  ' * tabs, "length =", length)
        if length == 1 or len(lst) == 0:
            return beg
        ret = []
        for item in lst:
            if item < beg[-1]:
                continue
            print()
            print('  ' * tabs, "item =", item)
            cur = beg[:]
            cur.append(item)
            print('  ' * tabs, "cur =", cur)
            if length == 2:
                ret.append(self.recurse(cur, [n for n in lst if n != item], length - 1, tabs + 1))
            else:
                ret.extend(self.recurse(cur, [n for n in lst if n != item], length - 1, tabs + 1))
        print()
        print()
        return ret

    def get_combinations(self, my_list):
        '''
        :param self:
        :param my_list: list
        :return: list[list]
        '''
        ret = []
        for length in range(len(my_list) + 1):
            if length == 0:
                ret.append([])
            elif length == 1:
                for item in my_list:
                    ret.append([item])
            else:
                for item in my_list:
                    ret.extend(self.recurse([item], [n for n in my_list if n != item], length, 0))
        return ret


print(MyList().get_combinations([2, 1, 3]))
