import unittest
"""
MxN矩阵, 将0元素的行和列都清零.
思路:
扫描一遍, 记录下0元素的位置, 然后把对应位置上的都给清零. 搞for循环的话, python肯定
是很慢的. 那就要关注一下numpy的一些更高效的操作了. 之前学numpy的时候, 重点放在了各个
功能的调用上. 以后的关注点, 则应该放在矩阵运算的优化上.
"""
import numpy as np
def zero_matrix(matrix):



class Test(unittest.TestCase):
    test_cases = [

    ]
    test_funcs = [
        # is_permutation
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()