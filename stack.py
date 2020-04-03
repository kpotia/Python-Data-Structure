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



s = Stack();
print(s.is_empty )

s.push('A0')
s.push('B0')
s.push('C1')

print(s.get_stack())
# s.pop()
print(s.peek())

s.push(3)
s.push(4)
s.push(2)
		
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.peek())
