import unittest
from linked_list import LinkedList
"""
删除未排序链表中的重复节点
思路:
这里难点根本就不在数据结构的操作上, 难在需要我自己来搭建起整个环境. 而这也恰恰是我想
锻炼的内容.
这里用的结构, 应该是没有空链表的.
"""

def remove_duplicate(ori_ll):
    seen = set()
    pointer = ori_ll.head
    if pointer == None:
        return str(ori_ll)
    seen.add(pointer.value)
    next_pointer = pointer.next
    while next_pointer:
        next_value = next_pointer.value
        if next_value in seen:
            next_pointer = next_pointer.next
            pointer.next = next_pointer
        else:
            pointer = next_pointer
            next_pointer = pointer.next
            seen.add(pointer.value)
    return str(ori_ll)

class Test(unittest.TestCase):
    a1 = LinkedList([1, 1, 2, 2, 3])
    a2 = LinkedList([1, 2, 3])
    b1 = LinkedList()
    b2 = LinkedList()

    test_cases = [
        [[a1], str(a2)],
        [[b1], str(b2)]
    ]
    test_funcs = [
        remove_duplicate
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
    unittest.main()