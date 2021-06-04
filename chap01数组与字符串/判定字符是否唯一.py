# 给一个字符串，来确定是否所有字符全都不同
import unittest
"""
这里是需要用到字典或者set的，主要就是一个hash的东西。能用dict或者set库函数是最好的。如果
不行，那可能需要调用python的hash函数来自己搞一个类似的数据结构。如果不能用自带的hash，
那你可以需要自己手写一个hash函数了。

这三种层次，我们在这里都实现一下。
"""
def is_unique(string):
    # 这里用内置set，O(n)
    a = set()
    # print(help(set)) # 这一招，在面试场合很适用。因为你能让别人相信你只是在看文档
    for i in string:
        if i in a:
            return False
        else:
            a.add(i)
    return True

def is_unique_noset(string):
    # O(n**2)的是很直接的。O(nlogn)是可以先排序，然后看重复
    ls = list(string)
    ls = sorted(ls)
    if len(ls) == 0:
        return True
    current = ls[0]
    for i in range(1, len(ls)):
        if current == ls[i]:
            return False
        else:
            current = ls[i]
    return True


def is_unique_hash(string):
    # 我们想手撸一个set，就是想实现O(1)来搞搜索。但是不会
    pass




class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
    ]
    test_funcs = [
        is_unique,
        is_unique_noset

    ]

    def test_method(self):
        for string, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(string), result)

if __name__ == "__main__":
    unittest.main()

