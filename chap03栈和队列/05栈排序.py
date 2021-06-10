import unittest
"""
要支持push, pop, peek, isEmpty. 但是pop出的东西要求是最小值. 而且只能用一个栈作为
额外的储存空间
思路:
一种是每进来一个, 我们都做出好的排序, 这样pop时方便; 另一种是进来时不做处理, pop时
要么做排序, 要么只找到那个最小的. 这个功能, 肯定是用堆, 或者说“树”这种结构好一些.
* 每次pop找最小, 这样复杂度是n**3(n个数, 每次pop都要n次比较, 然后移动n个元素), 舍弃
* 每进来一个都排序, 这样复杂度是: n**2 x logn (n个数, 每个push时要比较logn次, 移动n个数)
* 我猜用堆结构, n logn?
看了标答后:
标答采取了入栈时就排好序, 但是是直接用插入排序, 比我们用logn复杂度的排序代码量小很多.
所以直接实现一下吧.
"""


class SortedStack:
    def __init__(self) -> None:
        self.stack = []
        self.temp_stack = []

    def push(self, num):
        if self.isEmpty() or self.peek() >= num:
            self.stack.append(num)
        else:
            while not self.isEmpty() and self.peek() < num:
                self.temp_stack.append(self.stack.pop())
            self.stack.append(num)
            for _ in range(len(self.temp_stack)):
                self.stack.append(self.temp_stack.pop())

    def __len__(self):
        return len(self.stack)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


class Test(unittest.TestCase):
    test_cases = [

    ]
    test_funcs = [
        # is_permutation
    ]

    def _test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        assert len(queue) == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert len(queue) == 2

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert len(queue) == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4

if __name__ == "__main__":
    unittest.main()
