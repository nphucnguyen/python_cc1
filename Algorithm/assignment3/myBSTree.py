# binary search Tree cach dung
from node import Node
class BST:
    def __init__(self):
        self.root = None
    def insert(self,node):
        if self.root is None:
            self.root = node
        else:
            self._insert(node,self.root)
    #need to because we need recursive call
    def _insert(self,node,cur_node):
        if node.id<cur_node.id:
            if cur_node.left == None:
                cur_node.left = node
            else:
                self._insert(node,cur_node.left)
        elif node.id > cur_node.id:
            if cur_node.right == None:
                cur_node.right = node
            else:
                self._insert(node,cur_node.right)
        else:
            print ("ID already in list!")
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
    def search(self,id):
        if self.root!= None:
            return self._search(id,self.root)
        else:
            return False
    def _search(self,id,curNode):
        if id == curNode.id:
            return True
        elif id <curNode.id and curNode.left != None:
            return self._search(id,curNode.left)
        elif id >curNode.id and curNode.right != None:
            return self._search(id,curNode.right)
        return False
    def search_and_print(self,id):
        if self.root!= None:
            return self._search_and_print(id,self.root)
        else:
            return False
    def _search_and_print(self,id,curNode):
        if id == curNode.id:
            return curNode
        elif id <curNode.id and curNode.left != None:
            return self._search_and_print(id,curNode.left)
        elif id >curNode.id and curNode.right != None:
            return self._search_and_print(id,curNode.right)
        return False
    # def search_and_print(self,id):
    #     curNode = self.root
    #     if id == curNode.id:
    #         print(curNode)
    #     elif id <curNode.id and curNode.left != None:
    #         return self._search(id,curNode.left)
    #     elif id >curNode.id and curNode.right != None:
    #         return self._search(id,curNode.right)


    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)
    def _inorder_print(self, cur):
        if cur:
            self._inorder_print(cur.left)
            print(cur)
            self._inorder_print(cur.right)
    def deleteNode(self,id):
        temp_root = self.root
        self._deleteNode(temp_root,id)
    def _deleteNode(self, temp_root,id):
    
        if self.root is None:
            return self.root
    
        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if id < temp_root.id:
            temp_root.left = self._deleteNode(temp_root.left, id)
    
        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(id > temp_root.id):
            temp_root.right = self._deleteNode(temp_root.right, id)
    
        # If key is same as root's key, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if temp_root.left is None:
                temp = temp_root.right
                temp_root = None
                return temp
    
            elif temp_root.right is None:
                temp = temp_root.left
                temp_root = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(temp_root.right)
    
            # Copy the inorder successor's
            # content to this node
            temp_root.id = temp.id
            temp_root.name = temp.name
            temp_root.birthPlace = temp.birthPlace
            temp_root.birthDay = temp.birthDay
            
    
            # Delete the inorder successor
            temp_root.right = self._deleteNode(temp_root.right, temp.id)
    
        return temp_root
    def minValueNode(self,node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
# tree = BST()
# #tree = fillTree(tree)
# tree.root = Node(2)
# tree.root.left = Node(1)
# tree.root.right = Node(3)
# print(tree.is_bst_satisfied())
