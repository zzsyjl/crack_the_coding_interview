import unittest

from chap02链表.linked_list import LinkedList

"""
删除未排序链表中的重复节点
思路:
这里难点根本就不在数据结构的操作上, 难在需要我自己来搭建起整个环境. 而这也恰恰是我想
锻炼的内容.
进阶:
如果不使用临时缓冲区, 该怎么解决?
思路:
一开始我以为是要优化, 也就是说时间复杂度不能增加太多. 或者说, 真的是更好的解法. 
所以一开始没有思路, 因为这个问题真的是用set来解决是更好的. 但是这个加大难度的需求下,
你应该考虑用时间换空间的思路, 因为题目就是这么要求的.
有两种方法, 第一种是循环的过程中, 去看是否与前面的重复来删除本节点.
第二种是看与后面的是否重复来删除后面的节点. 先用后面这种吧.
问: 如何判断两个节点是否是同一个呢?
答: 用is?
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
    ori_ll.tail = pointer
    return str(ori_ll)


def remove_duplicate_followup(ori_ll):
    # pointer和nextpointer体系, 只能是删除nextpointer了. 发送旅客大幅拉升剪短发啦手机丢了卡就是对方离开撒到家阿斯顿咖啡呢
    pointer = ori_ll.head
    if pointer == None:
        return str(ori_ll)
    next_pointer = pointer.next
    while next_pointer:
        # 要从头开始, 循环到pointer, 判断是否与next_pointer的值相同
        runner = ori_ll.head
        is_dup = False
        while runner is not next_pointer:
            if runner.value == next_pointer.value:
                next_pointer = next_pointer.next
                pointer.next = next_pointer
                is_dup = True
                break
                # 如果有删除节点, 那么外层循环自动更新到下一个;
            runner = runner.next
        # 如果runner is nextpointer, 就要
        if not is_dup:
            pointer = next_pointer
            next_pointer = pointer.next
    ori_ll.tail = pointer
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
        remove_duplicate,
        remove_duplicate_followup
    ]

    def test_method(self):
        assert self.test_cases != []
        assert self.test_funcs != []
        for arguments, result in self.test_cases:
            for test_func in self.test_funcs:
                self.assertEqual(test_func(*arguments), result)


if __name__ == "__main__":
    # unittest.main()
    import sys
    print(sys.path)
