LINK = './input.txt'
from Node import Node
import Mylist
import Mystack
import MyQueue

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

class OperationToProduct:
    def __init__(self):
        self.llist = Mylist.LinkedList()
    def load(self):
        # load Data.txt
        # theo Linked list thu tu duoi
        while True:
            try:           
                f = open(input('Please enter the find path: '))
                print('The file is load successfully!')
                break
            except:
                print('File-path is not correct')
        board = f.readline()
        for line in f:
            self.llist.append(line.strip('\n'))
        

        f.close()
    def append(self):
        new_product = Node()
        self.llist.append_node(new_product)
    def display(self):
        self.llist.printList()
    def saveProductListToFile(self):
        f= open(input("Please enter the output path: "),'w')
        cur_node = self.llist.head
        while cur_node:
            f.write(f'{cur_node.data} \n')
            cur_node = cur_node.next
        print('The file is saved successfully!')
        f.close()
    def searchByID(self):
        id = input('Please enter the ID: ')
        cur_node = self.llist.head
        while cur_node:
            if cur_node.id == id:
                print(cur_node.data)
                return cur_node.data
                break
            cur_node = cur_node.next
        print('ID is not in the dataset!')


    def deletebyID(self):
        data = self.searchByID()
        print(data)
        if data == None:
            print('ID is not in the dataset!')
            return
        self.llist.delete_data(data)
        print('The product is removed from the dataset successfully!') 
    def sortByID(self):
        table = []
        cur_node = self.llist.head
        f_node = self.llist.head
        while cur_node:
            table.append(cur_node.data)
            cur_node = cur_node.next
        #sap xep data
        table.sort()
        index = 0
        while f_node:
            f_node.data = table[index]
            index +=1
            f_node.update()
            f_node = f_node.next
        
    def convertToBinary(self):
        data = self.searchByID()
        if data is None:
            return
        quantity = int(data.strip().split()[2])
        print('Convert quantity to binary: ', end = '')
        DecimalToBinary(quantity)
        print('\n')
    def loadToStackAndDisplay(self):
        self.stack_list = Mystack.Stack()
        while True:
            try:           
                f = open(input('Please enter the find path: '))
                print('The file is load successfully!')
                break
            except:
                print('File-path is not correct')
        board = f.readline()
        for line in f:
            self.stack_list.push(line.strip('\n'))
        f.close()
        while self.stack_list.root is not None:
            print (self.stack_list.pop())
    def loadToQueueAndDisplay(self):
        self.queue_list = MyQueue.Queue()
        while True:
            try:           
                f = open(input('Please enter the find path: '))
                print('The file is load successfully!')
                break
            except:
                print('File-path is not correct')
        board = f.readline()
        for line in f:
            self.queue_list.enQueue(line.strip('\n'))        
        f.close()
        while not self.queue_list.isEmpty():
            self.queue_list.deQueue()
    
    




        

         

# inventory = OperationToProduct()
# #inventory.load()
# # inventory.append()
# # inventory.append()
# #inventory.deletebyID()
# #inventory.sortByID()
# #inventory.convertToBinary()
# #inventory.display()
# inventory.loadToQueueAndDisplay()
# #nventory.saveProductListToFile()





