import unittest
from linked_list import LinkedList, LinkedListNode
"""
删除单向链表的某个中间节点, 其实头节点和尾节点也都是可以删的嘛.
思路:
就从前到后遍历, 遇到这个节点删除即可, 非常简单
"""

def remove_node(ll, node):
    pointer = ll.head
    if pointer is node:
        ll.head = pointer.next
        return ll
    next_pointer = pointer.next
    while next_pointer:
        if next_pointer is node:
            pointer.next = next_pointer.next
            return ll
        else:
            pointer = next_pointer
            next_pointer = next_pointer.next
    return ll



class Test(unittest.TestCase):
    a = LinkedList([1, 2, 3, 4, 5])
    node1 = LinkedListNode(1)
    node_head = a.head
    node_tail = a.tail
    node_middle = a.head.next


    test_cases = [
        [[a, node1], a],
        [[a, node_tail], LinkedList([1, 2, 3, 4])],
        [[a, node_head], LinkedList([2, 3, 4])],
        [[a, node_middle], LinkedList([3, 4])]
    ]
    test_funcs = [
        remove_node
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(str(test_func(*arguments)), str(result))

if __name__ == "__main__":
    unittest.main()