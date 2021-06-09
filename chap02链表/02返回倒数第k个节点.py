import unittest
from linked_list import LinkedList
"""
找出单向链表中倒数第k个节点
思路:
两个pointer之间相隔k-1的长度, 当前哨节点到最后了, 那么后面的自然就是target了
"""


def kth_to_the_last(ll, num):
    assert len(ll) >= num
    front = target = ll.head
    for i in range(num - 1):
        front = front.next
    while front.next:
        front = front.next
        target = target.next
    return target.value


class Test(unittest.TestCase):
    a1 = LinkedList([1, 1, 2, 2, 3])

    test_cases = [
        [[a1, 1], 3],
        [[a1, 5], 1]
    ]
    test_funcs = [
        kth_to_the_last
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)


if __name__ == "__main__":
    unittest.main()
