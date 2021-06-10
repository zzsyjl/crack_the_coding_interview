import unittest
from time import time
from collections import deque
"""
收容所只有猫和狗, 收养人需要严格遵循FIFO的规则. 实现enqueue, dequeueAny, dequeueDog
dequeueCat. 可以使用内置的链表
思路:
这个题不难, 我可以弄3个队列, 这里收的object需要有能力判断是猫还是狗. 我可以弄animal
类, 然后cat和dog都继承他们, 怎么弄判断方法呢?
所以来一个动物, 判断种类后, 就进入两个队列. 出队列的时候, 在相应的两个队列里调整即可.
那我为什么不只弄一个总队列呢? 这样才不会有数据冗余. 而且前一种方法里也是要到总队列里
一个一个找的
看了标答后:
标答就是我们的思路, 只不过弄得更正式了. 我们本来就是想弄‘dog’, ‘cat’等字符串的.
然后用字符串相等来判断. 而且人家也是弄了名字, 时间, 用isinstance来判断.
题目中说用链表, 不只是表示可以头尾删, 而且也可以中间任意位置删. 那么我们用dequeue也
这样任意删吧.
"""

class Animal:
	def __init__(self, name) -> None:
		self.admit_time = time()
		self.name = name

class Dog(Animal):
	pass

class Cat(Animal):
	pass

class AnimalShelter:
	def __init__(self) -> None:
		self.queue = deque()
		self.num_dog = 0
		self.num_cat = 0

	def enqueue(self, animal):
		self.queue.append(animal)
		if isinstance(animal, Cat):
			self.num_cat += 1
		else:
			self.num_dog += 1
	
	def dequeueAny(self):
		if self.num_dog + self.num_cat > 0:
			result = self.queue.popleft()
			if isinstance(result, Cat):
				self.num_cat -= 1
			else:
				self.num_dog -= 1
			return result
		else:
			return None

	def dequeueCat(self):
		if self.num_cat > 0:
			for i in range(len(self.queue)):
				if isinstance(self.queue[i], Cat):
					result = self.queue[i]
					self.queue.remove(result)
		else:
			return None

	def dequeueDog(self):
		if self.num_dog > 0:
			for i in range(len(self.queue)):
				if isinstance(self.queue[i], Dog):
					result = self.queue[i]
					self.queue.remove(result)
		else:
			return None

	def size(self):
		return self.num_cat + self.num_dog


class Test(unittest.TestCase):
	test_cases = [

	]
	test_funcs = [
		# is_permutation
	]

	def test_enqueue(self):
		animal_shelter = AnimalShelter()
		animal_shelter.enqueue(Cat("Fluffy"))
		animal_shelter.enqueue(Dog("Sparky"))
		animal_shelter.enqueue(Cat("Sneezy"))
		assert animal_shelter.size() == 3
	
	def _test_method(self):
		assert self.test_cases != []
		assert self.test_funcs != []
		for arguments, result in self.test_cases:
			for test_func in self.test_funcs:
				self.assertEqual(test_func(*arguments), result)

if __name__ == "__main__":
	unittest.main()