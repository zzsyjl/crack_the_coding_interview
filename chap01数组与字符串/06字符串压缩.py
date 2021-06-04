import unittest
"""
假设输入的字符串只是英文, 把“aaabb”压缩成“a3b2”, 如果长度没有缩短, 则返回原字符串
"""

def str_compress(string):
    if len(string) == 0:
        return string
    cur_char = string[0]
    cur_num = 1
    compressed_str = ''
    for ch in string[1:]:
        if ch == cur_char:
            cur_num += 1
        else:
            compressed_str += cur_char + str(cur_num)
            cur_char = ch
            cur_num = 1
    compressed_str += cur_char + str(cur_num)
    if len(compressed_str) < len(string):
        return compressed_str
    else:
        return string

class Test(unittest.TestCase):
    test_cases = [
        [['aaabb'], 'a3b2'],
        [['aabb'], 'aabb'],
        [[''], ''],
    ]
    test_funcs = [
        str_compress
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()