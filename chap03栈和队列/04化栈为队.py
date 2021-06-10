import unittest
"""
用两个栈来实现一个队列
思路:
队列就要满足先进先出, 一定要让最早压栈的跑到另一个栈的栈顶. 那么入队就是正常的入栈, 
出队时则要全都到另一个栈, 然后出栈即可出队了.
进阶:
我第一次的想法, 是work的. 但是如果add和remove交替进行的话, 效率非常低. 在test时看了
标准答案的思路, 很好! remove时, stack空了之后做一次倒腾. 然后add加addstack上, remove
操作在remove stack上.
"""

class MyQueue_obsolete:
    def __init__(self) -> None:
        self.add_stack = []
        self.remove_stack = []
        self.adding = True
    
    def add(self, item):
        if self.adding == False:
            for i in range(len(self.remove_stack)):
                self.add_stack.append(self.remove_stack.pop())
            self.adding = True
        self.add_stack.append(item)

    def remove(self):
        if self.adding == True:
            for i in range(len(self.add_stack)):
                self.remove_stack.append(self.add_stack.pop())
            self.adding = False
        if len(self) == 0:
            return None
        return self.remove_stack.pop()

    def peek(self):
        if self.adding == True:
            for i in range(len(self.add_stack)):
                self.remove_stack.append(self.add_stack.pop())
            self.adding = False
        return self.remove_stack[-1]

    def __len__(self):
        return len(self.add_stack) + len(self.remove_stack)


class MyQueue:
    def __init__(self) -> None:
        self.add_stack = []
        self.remove_stack = []

    def add(self, item):
        self.add_stack.append(item)

    def __len__(self):
        return len(self.add_stack) + len(self.remove_stack)

    def remove(self):
        if len(self) == 0:
            return None
        if len(self.remove_stack) == 0:
            for _ in range(len(self.add_stack)):
                self.remove_stack.append(self.add_stack.pop())
        return self.remove_stack.pop()

    def peek(self):
        if len(self) == 0:
            return None
        if len(self.remove_stack) == 0:
            for _ in range(len(self.add_stack)):
                self.remove_stack.append(self.add_stack.pop())
        return self.remove_stack[-1]


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

    test_cases = [([1, 2, 3]), ([-1, 0, 1]), (["a", "b", "c", "d", "e", "f"])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                assert len(q) == index
            for index, val in enumerate(sequence, start=1):
                q.remove()
                assert len(q) == len(sequence) - index

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert q.peek() == sequence[0]
            assert len(q) == len(sequence)

    def _test_shift_stacks(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert len(q.old_stack) == 0
            assert len(q.new_stack) == len(sequence)
            assert q.new_stack.peek() == sequence[-1]
            q._shift_stacks()
            assert len(q.old_stack) == len(sequence)
            assert len(q.new_stack) == 0
            assert q.old_stack.peek() == sequence[0]

    def test_peek(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
                assert q.peek() == sequence[0]
            q.remove()
            assert q.peek() == sequence[1]

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):  # noqa
                assert q.remove() == sequence[i]

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4
        q.add(101)
        assert q.peek() != 101

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert len(q) == 2
        assert q.remove() == 4
        assert q.remove() == 6
        assert len(q) == 0
        assert not q.remove()

if __name__ == "__main__":
    unittest.main()