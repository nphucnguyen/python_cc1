#stack by linked list
from Node import Node
# class StackNode:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
class Stack:
	def __init__(self):
		self.root = None
	def isEmpty(self):
		return True if self.root is None else False
    #them o dau
	def push (self,data):
		newNode = Node(data)
		newNode.next = self.root
		self.root = newNode
    #xuat o dau
	def pop(self):
		if self.isEmpty():
			return 'Stack clear'
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped
	def peek(self):
		if self.isEmpty():
			return 'Stack clear'
		return self.root.data
