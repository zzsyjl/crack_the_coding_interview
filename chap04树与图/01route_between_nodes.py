import unittest
from collections import deque
"""
节点间通路: 给一个有向图, 给两个节点, 找出这两点间是否存在路径.
思路:
首先我们还不知道这个有向图的数据结构呢. 那我们先考虑一下这个数据结构的设计思路吧.
图, 就是由点, 边, 边长所确定的. 所以稠密图我们可以用矩阵的方法表示, 稀疏图则用列表?
不管底层的结构是怎样, 我们在使用的时候, 必须要有的接口, 给定node的相邻点, 以及
对应的边长.
真正的数据结构:
graph = {
        "A": ["B", "C"],
        ...
        "R": ["P", "Q"],
    }
对有向图来说, 这样最简单得搞个字典嵌套列表就行了. 
发散: 
我也可以直接用列表嵌套列表, 这样首层列表内的index直接就是节点的编号了. 那么如果
我们想搞得自定义节点命名, 那就用字典嵌套列表即可.
如果加上边长, 用tuple(named tuple)最方便了!

思路:
这要在图上做搜索, 就是深度优先和广度优先嘛. dfs和bfs. 

结论:
果然bfs就是用队列来实现的. 没有问题!

dfs:
这里面
"""

def has_route_bfs(graph, node_a, node_b):
    deque_1 = deque([node_a])
    visited = {node_a}
    if node_b in deque_1:
        return True
    while deque_1:
        # 进队列时, 验证是否到b点, 以及对visited更新
        # 出队列时, 只是找到其下家, 然后这个就可以丢弃了
        popped = deque_1.popleft()
        children = graph[popped]
        if node_b in children:
            return True
        for child in children:
            if child not in visited:
                # 没由访问过, 加入访问过的集合, 同时加到队列里
                visited.add(child)
                deque_1.append(child)
    return False

def has_route_dfs(graph, node_a, node_b, visited=set()):
    if node_a == node_b:
        return True

    children = graph[node_a]
    for child in children:
        if has_route_dfs(graph, child, node_b):
            return True
    return False



        



class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "A", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    # def test_is_route(self):
    #     for [start, end, expected] in self.tests:
    #         actual = is_route(self.graph, start, end)
    #         assert actual == expected

    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = has_route_bfs(self.graph, start, end)
            assert actual == expected

    def test_is_route_dfs(self):
        for [start, end, expected] in self.tests:
            actual = has_route_dfs(self.graph, start, end)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()