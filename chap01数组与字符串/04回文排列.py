import unittest
"""
不是判断一个字符串是否是回文，而是看这个字符串的字符元素重新排列后，能否组成回文串。
书上给的示例忽略了大小写，无视空格。
思路1:
把所有的排列都得到，然后挨个判断是否回文。
思路2:
得到字符元素们，判断能否组成回文。偶数个的元素必然可以，所以可以忽略他们。
奇数个的只能有1个。那么可以用Counter. 也可以sort之后直接走一遍O(nlogn)。
Counter用了hash吧，所以是O(n).如果不用hash, 而是暴力查找的话, 就是O(n**2)的复杂度了.
"""
from collections import Counter
def can_huiwen_permutation(string):
    char_counter = Counter(string)
    if len(char_counter) == 0:
        return True
    odd_num = 0
    for key in char_counter:
        if char_counter[key] % 2 == 0:
            continue
        else:
            odd_num += 1
            if odd_num > 1:
                return False
    return True
        

class Test(unittest.TestCase):
    test_cases = [
        [['tactcoa'], True],
        [['12'], False]
    ]
    test_funcs = [
        can_huiwen_permutation
    ]

    def test_method(self):
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()