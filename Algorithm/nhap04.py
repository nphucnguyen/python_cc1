# #dung binary tree
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
class Stack:
    def __init__(self):
        self.items  = []
    def push (self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty ():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__ (self,root):
        self.root = Node(root)
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root,'')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root,'')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(self.root)
    #Pre_order traversal : first parent node, node left.. node right
    def preorder_print(self,start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left , traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def inorder_print(self,start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value)+ '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def postorder_print(self,start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal
    # level order need queue class
    def levelorder_print(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    def height(self,node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1+ max(left_height,right_height)
    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size +=1
                stack.push(node.left)
            if node.right:
                size +=1
                stack.push(node.right)
        return size
    def size_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)
       
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
print(tree.size())
print(tree.size_recursive(tree.root))


# binary search Tree cach dung
# class Node:
#     def __init__(self,value = None):
#         self.value = value
#         self.left = None
#         self.right = None
# class BST:
#     def __init__(self):
#         self.root = None
#     def insert(self,value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert(value,self.root)
#     #need to because we need recursive call
#     def _insert(self,value,cur_node):
#         if value<cur_node.value:
#             if cur_node.left == None:
#                 cur_node.left = Node(value)
#             else:
#                 self._insert(value,cur_node.left)
#         elif value > cur_node.value:
#             if cur_node.right == None:
#                 cur_node.right = Node(value)
#             else:
#                 self._insert(value,cur_node.right)
#         else:
#             print ("Value already in tree!")
#     def height(self):
#         if self.root != None:
#             return self._height(self.root,0)
#         else:
#             return 0
#     def _height(self,curNode,curHeight):
#         if curNode ==None:
#             return curHeight
#         leftHeight = self._height(curNode.left, curHeight+1)
#         rightHeight = self._height(curNode.right, curHeight+1)
#         return max(leftHeight,rightHeight)
#     def search(self,value):
#         if self.root!= None:
#             return self._search(value,self.root)
#         else:
#             return False
#     def _search(self,value,curNode):
#         if value == curNode.value:
#             return True
#         elif value <curNode.value and curNode.left != None:
#             return self._search(value,curNode.left)
#         elif value >curNode.value and curNode.right != None:
#             return self._search(value,curNode.right)
#         return False
#     def inorder_print(self):
#         if self.root:
#             self._inorder_print(self.root)
#     def _inorder_print(self, cur):
#         if cur:
#             self._inorder_print(cur.left)
#             print(str(cur.value))
#             self._inorder_print(cur.right)
#     def is_bst_satisfied(self):
#         if self.root:
#             is_satified = self._is_bst_satisfied(self.root)
#             if is_satified is None:
#                 return True
#             return False
#         return True
#     # method is the same with inorder_print
#     def _is_bst_satisfied(self,cur):
#         if cur.left:
#             if cur.value > cur.left.value:
#                 return self._is_bst_satisfied(cur.left)
#             else:
#                 return False
#         if cur.right:
#             if cur.value < cur.right.value:
#                 return self._is_bst_satisfied(cur.right)
#             else:
#                 return False



# def fillTree (tree, numElems = 10, maxInt= 100):
#     from random import randint
#     for _ in range(numElems):
#         curElem = randint(0,maxInt)
#         tree.insert(curElem)
#     return tree
# #     def inorder_print(self,start, traversal):
# #         if start:
# #             traversal = self.inorder_print(start.left, traversal)
# #             traversal += (str(start.value)+ '-')
# #             traversal = self.inorder_print(start.right, traversal)
# #         return traversal

# tree = BST()
# #tree = fillTree(tree)
# tree.root = Node(2)
# tree.root.left = Node(1)
# tree.root.right = Node(3)
# print(tree.is_bst_satisfied())


