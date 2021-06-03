# 给一个字符串，来确定是否所有字符全都不同
import unittest
"""
这里是需要用到字典或者set的，主要就是一个hash的东西。能用dict或者set库函数是最好的。如果
不行，那可能需要调用python的hash函数来自己搞一个类似的数据结构。如果不能用自带的hash，
那你可以需要自己手写一个hash函数了。

这三种层次，我们在这里都实现一下。
"""
def is_unique(string):
    a = set()
    # print(help(set)) # 这一招，在面试场合很适用。因为你能让别人相信你只是在看文档
    for i in string:
        if i in a:
            return False
        else:
            a.add(i)
    return True

# def is_unique_hash(string):



class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
    ]
    test_funcs = [
        is_unique,

    ]

    def test_func(self):
        for string, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(string), result)

if __name__ == "__main__":
    unittest.main()

