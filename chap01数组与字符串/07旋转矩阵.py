import unittest
"""
给定一幅NxN的图像, 每个像素占4个字节, 不占用额外内存, 将图像旋转90度.
思路:
这题不是出给python的, 是给c这些可以直接操作内存的语言出的. 我可以用numpy来做.
旋转90度, 本质上就是做四个一组的转换, 例如左上转到右上, 右上转到右下, 依此类推. 
以中心划分四象限, N是奇数和偶数不同情况, 有不同的轮转公式.
测试:
随机生成100x100x4和99x99x4的两个ndarray, 调用旋转库函数, 来验证我们自己的旋转算法
"""
import numpy as np
def rotate_img_90(ori_img):
    if len(ori_img) % 2 == 0: # 长度为偶数
        segment_length = int(len(ori_img) / 2)
        for i in range(segment_length):
            for j in range(segment_length):
                left_top = [i, j]
                right_top = [j, segment_length*2 - i - 1]
                # 整不下去了, 这个的corner case调整起来太麻烦, 而且现在我们也很难总
                # 结出好的规律, 那就暂时放弃这一题吧.
                # right_bottom = [segment_length*2 - i, segment_length*2 - j]


class Test(unittest.TestCase):
    def generate_cases(self, N):
        ori_img = np.random.randint(0, 255, size=(N, N, 4), dtype=np.uint8)
        target_img = np.rot90(ori_img, 1) # 文档里没说清楚是顺时针还是逆时针, 要做实验验证
        return ori_img, target_img

    ori100, target100 = generate_cases(100)
    ori99, target99 = generate_cases(99)
    test_cases = [
        [[ori100], target100],
        [[ori99], target99]
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