import unittest
"""
插入, 删除, 替换一个字符, 都属于一次编辑. 给两个字符串, 判断他们能否通过一次编辑得到
思路:
先判断两个字符串是否等长, 再分别遍历一下即可. 遍历时总共只有一次判断两个字符串是否相同. 
因此时间复杂度是O(n)
"""

def is_one_edit(string1, string2):
    if len(string1) != len(string2):
        short = string1 if len(string1)<len(string2) else string2
        long = string2 if len(string1)<len(string2) else string1
        # 考虑空字符串
        if len(short) == 0:
            return len(long) in [0, 1]
        # 遍历即可覆盖所有case
        for i in range(len(short)):
            if short[i] != long[i]:
                long_removed = long[:i] + long[i+1:]
                return short == long_removed
        return True
    else:
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return string1[i+1:] == string2[i+1:]
        return True

class Test(unittest.TestCase):
    test_cases = [
        [['pale', 'ple'], True],
        [['pale', 'pales'], True],
        [['pale', 'pple'], True],
        [['pale', 'pale'], True],
        [['pale', 'pppale'], False],
        # 考虑空字符串的情况
        [['', ''], True],
        [['', '1'], True],
        [['', '12'], False]
    ]
    test_funcs = [
        is_one_edit
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()
