import unittest
from collections import deque
"""
压栈其实就像堆盘子一样, 那么我们现在要把栈限制高度, 这样就是多个栈, 但是外在使用还是
一个栈. 同时要实现popAt的方法, 能够指定pop的栈. 疑问: 需不需要在前面有空隙时填补呢?
下一次push, 给push到前面的空隙还是末尾呢?
看了答案, 确实是补空隙的.
思路:
初始化时设定单个栈的capacity, 同时要记录当前有几个栈, 一个栈删干净后, 也还是要保留,
除非上一个栈也是不满的. 这样当本栈满了的时候, 就要直接开一个新栈了.
那么补空隙就需要对列表的左端进行操作, 所以这里用deque是更好的.


"""

class SetOfStacks:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.idx_of_top_stack = 0
        self.stacks = [deque()]

    def push(self, item):
        if len(self.stacks[self.idx_of_top_stack]) >= self.capacity:
            self.stacks.append(deque())
            self.idx_of_top_stack += 1
        self.stacks[self.idx_of_top_stack].append(item)

    def pop(self):
        if len(self.stacks[self.idx_of_top_stack]) == 0:
            if len(self.stacks) == 1:
                return None
            self.stacks.pop()
            self.idx_of_top_stack -= 1
        return self.stacks[self.idx_of_top_stack].pop()

    def pop_at(self, idx):
        if idx >= self.idx_of_top_stack:
            return self.pop()
        result = self.stacks[idx].pop()
        try:
            for i in range(idx, self.idx_of_top_stack):
                self.stacks[i].append(self.stacks[i+1].popleft())
        except:
            # 如果最后的栈是空栈, 那么前面popleft就会报错, 这里只需要删掉这个栈即可
            self.stacks.pop()
            self.idx_of_top_stack -= 1
        return result

        
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

    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        assert lst == list(reversed(range(35)))

    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        assert lst == list(range(4, 35))

if __name__ == "__main__":
    unittest.main()