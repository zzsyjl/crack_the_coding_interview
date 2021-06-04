import unittest
"""
将字符串中的空格替换成%20。这个我们直接用replace就好了吧？
"""

# def is_permutation(string1, string2):

def urlization(string):
    print(string)
    return string.replace(' ', '%20')

class Test(unittest.TestCase):
    test_cases = [
        (('1 2 3',), '1%202%203'), # 我print这个东西，输出就是1%202%203,没有特殊格式，为什么这里显示不同的颜色呢
        ((' 1   2   333 4',), '%201%20%20%202%20%20%20333%204'), # 你输入的tab键，背后都被转成一定长度的空格了
        (('\n\t1 2\t',), '\n\t1%202\t')
    ]
    test_funcs = [
        urlization
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()