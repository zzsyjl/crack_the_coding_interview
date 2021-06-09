from typing import Counter
import unittest
"""
要求这个栈能够以O(1)的复杂度返回最小值
思路:
一开始, 我以为记录一下min值不就行了? 但是我们这里的栈是一个动态的, push之后可以轻松
更新最小值, 但是pop之后, 原来的最小值不在了, 你的方法就失效了.
所以, 最粗暴的方法是多建一个栈, 存放当前的最小值, 那么同步push和pop即可. 空间复杂度也是
O(n). 我们当然是能够优化的, 但是空间复杂度还是那么多.
push的时候, 更大值的话, 就不需要对最小值栈做push. 所以这个最小值栈一定是个递减的栈.
pop的时候, 如果是更大的值, 也是不需要更新最小值栈. 
如果小或者相等的时候, 就去更新最小值栈.

"""

class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
    
    def push(self, num):
        current_min = self.min_stack[-1] if self.stack else float('inf')
        if num <= current_min:
            self.stack.append(num)
            self.min_stack.append(num)
        else:
            self.stack.append(num)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def minimum(self):
        if self.stack:
            return self.min_stack[-1]
        else:
            return None


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
    # unittest.main()
    newstack = MinStack()
    assert newstack.minimum() is None

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1