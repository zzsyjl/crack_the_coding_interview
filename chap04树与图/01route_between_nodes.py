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
"""

def has_route_bfs(graph, node_a, node_b):
	deque_1 = deque(graph[node_a])
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
	unittest.main()