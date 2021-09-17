from collections import deque
import sys
sys.path.append(
    '/Users/jlyang/python_projects/crack_the_coding_interview/chap02链表')
from linked_list import LinkedList
import unittest
"""
特定深度节点链表. 给定一个二叉树, 设计一个算法, 创建每个深度上的节点链表
分析:
这个东西应该也是很有用的. 我用层遍历的思路, 每次集体出一层的时候, 再集体进一层.
"""

from collections import deque
import sys
sys.path.append(
    '/Users/jlyang/python_projects/crack_the_coding_interview/chap02链表')


class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return '%s' % self.name


def create_node_list_by_depth(root):
    lists = []
    queue = deque([root])
    while len(queue) > 0:
        llist = LinkedList()
        length = len(queue)
        for _ in range(length):
            popped = queue.popleft()
            llist.add(popped)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        lists.append(llist)
    return lists


def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    for i in levels:
        print(i)


if __name__ == "__main__":
    example()
