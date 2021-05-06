# lab 6.1
# https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/1059946


# lab 6.2
# https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/805177
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.data, end= ' ')
            curNode = curNode.next
    def append(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        curNode = self.head
        while curNode.next:
            curNode = curNode.next
        curNode.next = newNode
    def appends(self,lst):
        for newData in lst:
            self.append(newData)
    def len(self):
        if self.head is None:
            return 0
        curNode = self.head
        n= 0
        while curNode:
            n +=1
            curNode = curNode.next
        return n
    def addpos(self,pos,data):
        if pos > self.len():
            return
        n = self.len()
        newNode = Node(data)
        curNode = self.head
        if pos == 0:
            newNode.next = curNode
            self.head = newNode
            return
        for i in range(n):
            if i+1 == pos:
                newNode.next = curNode.next
                curNode.next = newNode
                return
            curNode = curNode.next
    def remove_pos(self,pos):
        if self.head is None:
            return
        curNode = self.head
        if pos == 0:
            self.head = curNode.next
            curNode = None
            return
        cur = 0
        while curNode.next:
            if cur+1 == pos:
                delNode = curNode.next
                curNode.next = delNode.next
                delNode = None
                return
            curNode = curNode.next
            cur +=1
    def index_value(self,index):
        if self.head is None:
            return
        curNode = self.head
        cur = 0
        while curNode:
            if cur == index:
                return curNode.data
            curNode = curNode.next
            cur +=1
        return None
    def replace(self,index,data):
        if self.head is None:
            return
        curNode = self.head
        cur = 0
        while curNode:
            if cur == index:
                curNode.data = data
            curNode = curNode.next
            cur +=1
    def removeNode(self,node):
        if self.head is None:
            return
        if self.head.next is None:
            if node == self.head:
                self.head == None
                return
            return
        if node == self.head:
            self.head = self.head.next
            return
        prevNode = None
        curNode = self.head
        while curNode:
            if curNode == node:
                prevNode.next = curNode.next
                curNode = None
                return
            prevNode = curNode
            curNode = curNode.next
    def remove_all_greaterthanpos(self,pos):
        data = self.index_value(pos)
        if data is None:
            return
        curNode = self.head
        while curNode:
            if curNode.data > data:
                self.removeNode(curNode)
            curNode = curNode.next
        
        

        
        
            

        
        
        




            

#n = int(input())
#lst = list(map(int,input().strip().split()))
lst = [1,2,3,4]
llist = LinkedList()
llist.appends(lst)
llist.remove_all_greaterthanpos(1)
llist.printList()
