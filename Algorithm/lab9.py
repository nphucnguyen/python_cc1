# duyet cay (chua xong, code chua chay)
# input : dòng đầu số đỉnh
# các dòng tiếp theo: giá trị key - index con trái - index con phải
class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root = None):
        self.root = Node(root)
    def find_root(self,data_arr):
        head_arr = set(x[0] for x in data_arr)
        tail_arr = set(x[1] for x in data_arr).union(set(x[2] for x in data_arr))
        root = head_arr.difference(tail_arr).pop()
        self.root = Node(root)
        temp = self.root
        return temp
    def connectFromBegin(self,data_arr):
        temp = self.root
        self._connect(temp,data_arr)
    def _connect(self,node,data_arr):
        for arr in data_arr:
            if arr[0] == node.data:
                if arr[1] != -1:
                    temp_left = Node(arr[1])
                    node.left = temp_left
                    self._connect(temp_left,data_arr)
                if arr[2] != -1:
                    temp_right = Node(arr[2])
                    Node.right = temp_right
                    self._connect(temp_right,data_arr)
            break
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root,'')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root,'')
        # elif traversal_type == 'levelorder':
        #     return self.levelorder_print(self.root)
    #Pre_order traversal : first parent node, node left.. node right
    def preorder_print(self,start, traversal):
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.preorder_print(start.left , traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def inorder_print(self,start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data)+ '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def postorder_print(self,start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal
    # level order need queue class
    # def levelorder_print(self,start):
    #     if start is None:
    #         return
    #     queue = Queue()
    #     queue.enqueue(start)
    #     traversal = ''
    #     while len(queue) > 0:
    #         traversal += str(queue.peek()) + '-'
    #         node = queue.dequeue()
    #         if node.left:
    #             queue.enqueue(node.left)
    #         if node.right:
    #             queue.enqueue(node.right)
    #     return traversal




    
    



n = int(input('Please enter the number of nodes: '))
data_arr = [list(map(int,input('Please enter de node: ').strip().split())) for _ in range(n)]
print(data_arr)
tree = BinaryTree()
tree.find_root(data_arr)
tree.connectFromBegin(data_arr)
print(tree.root.data)
print(tree.root.left.data)
print(tree.root.left)
print(tree.root.right.data)
print(tree.root.right)