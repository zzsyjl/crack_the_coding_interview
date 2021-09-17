import unittest
"""
给两个字符串，判断能否经过重新排列，让一个变成另一个。我们也要测试对中文字符的支持。
这次把中文字符给测了，但以后不必了，因为本质上都是unicode，肯定都支持的。而testcase则
要都重新写一遍，没有必要。
"""

def is_permutation(string1, string2):
    """都按照某种规则重新排列，然后直接比较即可，可以使用sorted内置函数
    """
    string1_sorted = sorted(list(string1))
    string2_sorted = sorted(list(string2))
    return string1_sorted == string2_sorted

def is_permutation_set(string1, string2):
    string1_sorted = set(list(string1))
    string2_sorted = set(list(string2))
    return string1_sorted == string2_sorted


class Test(unittest.TestCase):
    test_cases = [
        (('abcd', 'dbca'), True),
        (('abcd', '1234'), False),
        (('abcd', 'abcde'), False),
        (('我爱你！', '你！爱我'), True),
        (('我爱你', '我爱你！'), False),
        (('', ''), True),
        (('', 'asd'), False)
    ]
    test_funcs = [
        is_permutation,
        is_permutation_set
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()