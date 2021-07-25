import unittest
"""
最小高度树. 给定一个有序整数数组, 元素各不相同且按升序排列. 编写一个算法, 创建一个高
度最小的二叉搜索树
分析:
这个数组的性质很好. 我直接就能知道每层应该是什么. 而且是用分而治之的递归方法即可.

边界条件:
当这个数组长度为3时, 还是可以继续分;
长度为2时, midnode和left没问题, 右边就变成空列表了, 但也应看成是继续分;
长度为1时, 极端一点, 我还是可以继续分, 只不过左右两边都是空列表;
    但是, 这就会导致列表切片时超出范围了.
    
"""

class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.key}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()

def bst_from_ascend_array(ascend_array):
    length = len(ascend_array)
    if length == 1:
        return TreeNode(ascend_array[0])
    if length == 0:
        return None
    mid_idx = length//2
    mid = ascend_array[mid_idx] # 长度为3, 取中间; 长度为4, 取中右
    mid_node = TreeNode(mid)
    mid_node.left = bst_from_ascend_array(ascend_array[: mid_idx])
    mid_node.right = bst_from_ascend_array(ascend_array[mid_idx+1: ])
    return mid_node





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
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 
    15, 18, 22, 43, 144, 515, 4123]
    tree_root = bst_from_ascend_array(test_array)
    print(tree_root)