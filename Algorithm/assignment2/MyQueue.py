#queue by linked list
from Node import Node
# class Node:
# 	def __init__(self,data):
# 		self.data= data
# 		self.next = None
class Queue:
	def __init__ (self):
		self.front = self.rear = None
	def isEmpty(self):
		return self.front == None
	def enQueue(self, data):
		temp = Node(data)
		if self.rear == None:
			self.front = self.rear = temp
			return
		self.rear.next = temp
		self.rear = temp
	def deQueue(self):
		if self.isEmpty():
			return
		temp = self.front
		print(temp.data)
		self.front = temp.next
		if self.front == None:
			self.rear = None
