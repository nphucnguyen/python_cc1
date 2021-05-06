
# # singe linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def printList(self):
#         cur_node = self.head
#         while cur_node:
#             print(cur_node.data,end=' ')
#             cur_node = cur_node.next
            
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         cur_node = self.head
#         #move to the last node
#         while cur_node.next:
#             #khi di chuyển nên cho biến tạm
#             cur_node = cur_node.next
#         cur_node.next = new_node
#     #add node in the head
#     def prepend(self,data):
#         head_node = Node(data)
#         head_node.next = self.head
#         self.head = head_node
#     #insert after specific Node
#     def insert_after_node(self,prev_node,data):
#         #check prev_node in linklist
#         if not prev_node:
#             print("\nPrevious node is not in the list")
#             return
#         new_node = Node(data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
#     def delete_node(self,data):
#         cur_node = self.head
#         if cur_node and cur_node.data == data:
#             self.head = cur_node.next
#             #thoát khỏi data đó, k phải xóa data đó đi
#             cur_node = None
#             return
#         #check data in llist 
#         while cur_node and cur_node.data !=data:
#             prev = cur_node
#             cur_node = cur_node.next
#         if cur_node is None:
#             return
#         prev.next = cur_node.next
#         #k tro vao data do nua
#         cur_node = None
#     #position 0,1,2,..
#     def delete_node_atpos(self,pos):
#         cur_node=self.head
#         if pos == 0:
#             self.head = cur_node.next
#             cur_node = None
#             return
#         prev = None
#         count = 0
#         #check position
#         while cur_node and count !=pos:
#             prev = cur_node
#             cur_node = cur_node.next
#             count +=1
#         if cur_node is None:
#             return
#         prev.next = cur_node.next
#         cur_node = None
#     def len(self):
#         count = 0
#         cur_node = self.head
#         while cur_node:
#             count +=1
#             cur_node = cur_node.next
#         return count
#     def swap_nodes(self,key1,key2):
#         if key1 == key2:
#             return
#         cur1 = self.head
#         cur2 = self.head
#         #tim node chua key 1 va key2
#         while cur1 and cur1.data !=key1:
#             cur1 = cur1.next
#         print(cur1.data)
#         while cur2 and cur2.data !=key2:
#             cur2 = cur2.next
#         print(cur2.data)
#         #check neu 1 trong 2 la none
#         if not cur1 or not cur2:
#             return
#         cur1.data , cur2.data = cur2.data , cur1.data
#     def reverse_all_nodes(self):
#         prev = None
#         cur = self.head
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
#         self.head = prev
#     def merge_2_sorted_llist(self,llist):
#         #P for cur_node1, Q for cur_node2, s is the curr of 2
#         p =self.head
#         q = llist.head
#         s = None
#         #check empty list
#         if not p:
#             return q
#         if not q:
#             return p
#         if p and q:
#             if p.data <= q.data:
#                 s=p
#                 p = s.next
#             else:
#                 s = q
#                 q = s.next
#             new_head = s
#         #operate 2 element
#         while p and q:
#             if p.data <=q.data:
#                 s.next = p
#                 p = p.next
#                 s = s.next
#             else:
#                 s.next = q
#                 s = s.next
#                 q = q.next
#         #1 of 2 llist to end
#         if not p:
#             s.next = q
#         if not q:
#             s.next = p
#         return new_head
#     def remove_duplicates(self):
#         cur = self.head
#         prev = None
#         dup_values = dict()
#         while cur:
#             if cur.data in dup_values:
#                 #remove duplicte
#                 prev.next = cur.next
#                 cur = prev.next
#             else:
#                 dup_values[cur.data] = 1
#                 prev = cur
#                 cur = cur.next
#     # node co thu tu dem tu cuoi
#     def nth_from_last(self,n):
#         #method1
#         total_len = self.len()
#         location = total_len -n
#         index =0
#         cur = self.head
#         if location < 0:
#             return
#         while index != location:
#             cur = cur.next
#             index +=1
#         return cur.data
#     def count_occurences_iterative(self,data):
#         count = 0
#         cur = self.head
#         while cur:
#             if cur.data == data:
#                 count +=1
#             cur = cur.next
#         return count
#     def count_occurences_recursive(self,node, data):
#         if not node:
#             return 0
#         if node.data == data:
#             return 1 + self.count_occurences_recursive(node.next,data)
#         else:
#             return self.count_occurences_recursive(node.next,data)
#     # 1 2 3 4 5 6 thanh 5 6 1 2 3 4 o vi tri 4
#     def rotate_data(self,data):
#         temp_head = self.head
#         cur = self.head
#         prev = None
#         while cur:
#             if cur.data == data:
#                 if not cur.next:
#                     return
#                 temp_rotate = cur
#             prev = cur
#             cur = cur.next
#         prev.next = temp_head
#         self.head = temp_rotate.next
#         temp_rotate.next = None
#     # Palindrome là vd rar , abcba, tuc la viet nguoc lai y chang
#     def is_palindrome(self):
#         # # method 1: using string
#         # s = ''
#         # p = self.head
#         # while p:
#         #     s += str(p.data)
#         #     p = p.next
#         # return s == s[::-1]
#         # method 2: using stack
#         p = self.head
#         s = []
#         while p:
#             s.append(p.data)
#             p = p.next
#         p = self.head
#         while p:
#             data = s.pop()
#             if p.data != data:
#                 return False
#             p=p.next
#         return True
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(2)
# llist.append(1)
# print(llist.is_palindrome())
# llist.printList()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
# class Double_linked_list:
#     def __init__(self):
#         self.head = None
#     def append(self,data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node = Node(data)
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             new_node.prev = cur
#             cur.next = new_node        
#     def prepend(self,data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#     def printList(self):
#         cur = self.head
#         while cur:
#             print(cur.data)
#             cur = cur.next
#     def add_after_node(self,key, data):
#         cur = self.head
#         while cur:
#             if cur.next is None and cur.data == key:
#                 self.append(data)
#                 return
#             elif cur.data == key:
#                 new_node = Node(data)
#                 nxt = cur.next
#                 cur.next = new_node
#                 new_node.prev = cur
#                 new_node.next = nxt
#                 nxt.prev = new_node
#             cur = cur.next
#     def add_before_node(self, key, data):
#         cur = self.head
#         while cur:
#             if cur.prev is None and cur.data == key:
#                 self.prepend(data)
#                 return
#             elif cur.data ==key:
#                 new_node = Node(data)
#                 prev = cur.prev
#                 prev.next = new_node
#                 new_node.prev = prev
#                 new_node.next = cur
#                 cur.prev = new_node
#     def delete_node(self,key):
#         cur = self.head
#         while cur:
#             if cur.data == key and cur == self.head:
#                 #case 1
#                 if not cur.next:
#                     cur = None
#                     self.head = None
#                     return
#                 # case 2
#                 else:
#                     nxt = cur.next
#                     self.head = nxt
#                     nxt.prev = None
#                     cur.next = None
#                     cur = None
#                     return
#             elif cur.data == key:
#                 # case 3
#                 if not cur.next:
#                     pre = cur.prev
#                     pre.next = None
#                     cur.prev = None
#                     cur = None
#                     return
#                 # case 4 common
#                 else:
#                     pre = cur.prev
#                     nxt = cur.next
#                     pre.next = nxt
#                     nxt.pre = pre
#                     cur.prev = None
#                     cur.next = None
#                     cur = None
#                     return
#             cur = cur.next
#     def reverse(self):
#         cur = self.head
#         while cur:
#             if cur.next is None:
#                 self.head = cur
#             cur.next , cur.prev = cur.prev , cur.next
#             cur = cur.prev
                    
                
            




# dllist = Double_linked_list()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
# dllist.reverse()
# dllist.printList()


'''
#stack by array
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def getStack(self):
        return self.items
    def isEmpty(self):
        return self.items == []
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
s = Stack()
s.push(1)
s.push('Nguyen')
print(s.getStack())
'''




#stack by linked list
class StackNode:
	def __init__(self,data):
		self.data = data
		self.next = None
class Stack:
	def __init__(self):
		self.root = None
	def isEmpty(self):
		return True if self.root is None else False
	def push (self,data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
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

#Queue by list
# class Queue:
# 	def __init__(self, capacity):
# 		self.front = self.size = 0
# 		self.rear = capacity -1
# 		self.Q = [None]*capacity
# 		self.capacity = capacity
# 	def isFull(self):
# 		return self.size == self.capacity
# 	def isEmpty(self):
# 		return self.size == 0
# 	def enQueue(self,item):
# 		if self.isFull():
# 			print("Full")
# 			return
# 		self.rear = (self.rear +1) % self.capacity
# 		self.Q[self.rear] = item
# 		self.size +=1
# 	def deQueue(self):
# 		if self.isEmpty():
# 			print("Empty")
# 			return
# 		self.front = (self.front + 1) % self.capacity
# 		self.size -=1
# 	def get_front(self):
# 		if self.isEmpty():
# 			print('Queue is empty')
# 		print(self.Q[self.front])
# 	def get_rear(self):
# 		if self.isEmpty():
# 			print('Queue is empty')
# 		print(self.Q[self.rear])



#queue by linked list
# class Node:
# 	def __init__(self,data):
# 		self.data= data
# 		self.next = None
# class Queue:
# 	def __init__ (self):
# 		self.front = self.rear = None
# 	def isEmpty(self):
# 		return self.front == None
# 	def enQueue(self, item):
# 		temp = Node(item)
# 		if self.rear == None:
# 			self.front = self.rear = temp
# 			return
# 		self.rear.next = temp
# 		self.rear = temp
# 	def deQueue(self):
# 		if self.isEmpty():
# 			return
# 		temp = self.front
# 		self.front = temp.next
# 		if self.front == None:
# 			self.rear = None
		