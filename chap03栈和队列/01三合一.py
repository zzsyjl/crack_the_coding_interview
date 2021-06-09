import unittest
"""
用一个数组实现3个栈
思路:
一个线性的数组, 是怎么实现这个的呢?
可以加一个计数器, 每个栈都有计数. 就弄三个平行的吧.
我们可以增加一下难度, 把3换成n, 那么这样就需要不固定数量的函数了.
"""


class ManyStacksInOne:
    def __init__(self, n) -> None:
        self.n = n
        self.array = []
        self.len_max = 0
        self.lens = [0] * n

    def push(self, i, num):
        len_i = self.lens[i]
        if len_i == self.len_max:
            self.array.extend([None]*self.n)
            self.len_max += 1
        self.array[len_i * self.n + i] = num
        self.lens[i] += 1

    def pop(self, i):
        len_i = self.lens[i]
        if len_i == self.len_max and sum(self.lens >= len_i) > 1:
            result = self.array[self.n * (len_i-1) + i]
            del self.array[-self.n:]
            return result
        else:
            result = self.array[self.n * (len_i-1) + i]
            self.array[self.n * (len_i-1) + i] = None
            return result


# class Test(unittest.TestCase):


#     test_cases = [
#     ]
#     test_funcs = [
#         # is_permutation
#     ]
#     def test_method(self):
#         assert self.test_cases != []
#         assert self.test_funcs != []
#         for arguments, result in self.test_cases:
#             for test_func in self.test_funcs:
#                 self.assertEqual(test_func(*arguments), result)
if __name__ == "__main__":
    # unittest.main()
    a = ManyStacksInOne(3)
    a.push(0, 0)
    assert a.array == [0, None, None]
    a.push(0, 1)
    assert a.array == [0, None, None, 1, None, None]
    assert a.pop(1) == None, a.array == [0, None, None, 1, None, None]
    a.push(2, 33)
    assert a.array == [0, None, 33, 1, None, None]
