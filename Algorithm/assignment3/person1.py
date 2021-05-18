# import Mylist
# import Mystack
# import MyQueue
from node import Node
from myBSTree import BST
from myQueue import Queue
class Operation:
    def __init__(self):
        self.bList = BST()
    def load(self):
        # load data.txt
        while True:
            try:           
                f = open(input('Please enter the find path: '))
                print('The file is load successfully!')
                break
            except:
                print('File-path is not correct')
        board = f.readline()
        for line in f:
            id, name, birthDay , birthPlace = line.strip().split()
            new_employee = Node(id,name,birthDay,birthPlace)
            self.bList.insert(new_employee)

        f.close()
    def insert(self):
        id = input('Please insert the new ID: ')
        if self.bList.search(id):
            print('This ID has been chosen, please choose another ID!')
            self.insert()
        else:
            name = input('Please insert the Name: ')
            birthPlace = input('Please insert the birth place: ')
            birthDay = input('Please insert Birth of Day: ')
            new_employee = Node(id,name,birthDay,birthPlace)
            self.bList.insert(new_employee)
            print(f'''New ID: {id}
            Name: {name}
            Birthplace: {birthPlace}
            Day of Birth: {birthDay}
            ''')
    def inorder_traverse(self):
        self.bList.inorder_print()


    # def breath_first_traverse(self):
    #     temp_node = self.bList.root
    #     queue_list = [temp_node]
    #     while queue_list != []:
    #         if queue_list[0] is None:
    #             return
    #         else:
    #             print(queue_list[0])
    #             if queue_list[0].left != None:
    #                 queue_list.append(queue_list[0].left)
    #             if queue_list[0].right != None:
    #                 queue_list.append(queue_list[0].right)
    #             queue_list.pop(0)
    
    def breath_first_traverse(self):
        temp_node = self.bList.root
        queue_list = Queue()
        queue_list.enqueue(temp_node)
        while not queue_list.is_empty():
            if queue_list.is_empty():
                return
            else:
                print(queue_list.peek())
                if queue_list.peek().left != None:
                    queue_list.enqueue(queue_list.peek().left)
                if queue_list.peek().right != None:
                    queue_list.enqueue(queue_list.peek().right)
                queue_list.dequeue()
    def searchByID(self):
        id = input("Please insert the ID: ")
        if self.bList.search(id):
            print(self.bList.search_and_print(id))
        else:
            print('The searched ID is not valid')
    def deletebyID(self):
        id = input('Please insert the ID: ')
        if not self.bList.search(id):
            print('The search ID is not valid')
        else:
            print(f'Delete the person with ID = {id}')
            self.bList.search_and_print(id)
            self.bList.deleteNode(id)



