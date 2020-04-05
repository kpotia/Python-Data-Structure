"""
	Python stack data structure 
	FILO: First In Last Out

"""

class Stack():
	"""docstring for Stack"""
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def pop(self):
		return self.items.pop()

	def get_stack(self):
		return self.items

	def search(self,item):
		if item in self.items:
			return item 
		else: return False
