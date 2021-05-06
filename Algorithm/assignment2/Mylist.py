# singe linked list
from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        #move to the last node
        while cur_node.next:
            #khi di chuyển nên cho biến tạm
            cur_node = cur_node.next
        cur_node.next = new_node
    def append_node(self,new_node):
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        #move to the last node
        while cur_node.next:
            #khi di chuyển nên cho biến tạm
            cur_node = cur_node.next
        cur_node.next = new_node

    #add node in the head
    def prepend(self,data):
        head_node = Node(data)
        head_node.next = self.head
        self.head = head_node
    #insert after specific Node
    def insert_after_node(self,prev_node,data):
        #check prev_node in linklist
        if not prev_node:
            print("\nPrevious node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_data(self,data):
        cur_node = self.head
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            #thoát khỏi data đó, k phải xóa data đó đi
            cur_node = None
            return
        #check data in llist 
        while cur_node and cur_node.data !=data:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        #k tro vao data do nua
        cur_node = None
    #position 0,1,2,..
        
    def delete_node_atpos(self,pos):
        cur_node=self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 0
        #check position
        while cur_node and count !=pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
    def len(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count +=1
            cur_node = cur_node.next
        return count
    def swap_nodes(self,key1,key2):
        if key1 == key2:
            return
        cur1 = self.head
        cur2 = self.head
        #tim node chua key 1 va key2
        while cur1 and cur1.data !=key1:
            cur1 = cur1.next
        print(cur1.data)
        while cur2 and cur2.data !=key2:
            cur2 = cur2.next
        print(cur2.data)
        #check neu 1 trong 2 la none
        if not cur1 or not cur2:
            return
        cur1.data , cur2.data = cur2.data , cur1.data
    def merge_2_sorted_llist(self,llist):
        #P for cur_node1, Q for cur_node2, s is the curr of 2
        p =self.head
        q = llist.head
        s = None
        #check empty list
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s=p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        #operate 2 element
        while p and q:
            if p.data <=q.data:
                s.next = p
                p = p.next
                s = s.next
            else:
                s.next = q
                s = s.next
                q = q.next
        #1 of 2 llist to end
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
