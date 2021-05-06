# Min heap
class MinHeap:
    def __init__(self,capacity):
        self.storage = [0]* capacity
        self.capacity = capacity
        self.size = 0
    def getParentIndex(self,index):
        return (index -1)//2
    def getLeftChildIndex(self,index):
        return 2*index +1
    def getRightChildIndex(self,index):
        return 2*index +2
    def hasParent(self,index):
        return self.getParentIndex(index) >=0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) <self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]
    def isFull(self):
        return self.size == self == self.capacity
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    def insert(self,data):
        if self.isFull():
            print('Heap is full, can not be storage')
            return
        self.storage[self.size] = data
        self.size +=1
        self.heapifyUp()
    def heapifyUp(self):
        # tro ve index cua so vua duoc them
        index = self.size -1
        #dieu chinh vi tri cac du lieu
        while(self.hasParent(index) and self.parent(index)> self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)
    def removeMin(self):
        if self.size == 0:
            return
        data = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.size -=1
        self.heapifyDown()
        return data
    def heapifyDown(self):
        index =0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if(self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex



# # heap sort dung heapq (min heap)
# from heapq import heappush, heappop, heapify
# class MinHeap:
#     def __init__(self):
#         self.heap = []
#     def parent(self,i):
#         return (i-1)//2
#     def insertKey (self,k):
#         heappush(self.heap,k)
#     def decreaseKey(self,i, new_val):
#         self.heap[i] =new_val
#         while(i !=0 and self.heap[self.parent(i)] > self.heap[i]):
#             #swap
#             self.heap[i] , self. heap[self.parent(i)] = self. heap[self.parent(i)] , self.heap[i]
#     def extractMin(self):
#         return heappop(self.heap)
#     def deleteKey(self, i):
#         self.decreaseKey(i,float('-inf'))
#         self.extractMin()
#     def getMin(self):
#         return self.heap[0]

# heapObj = MinHeap()
# heapObj.insertKey(3)
# heapObj.insertKey(2)
# heapObj.deleteKey(1)
# heapObj.insertKey(15)
# heapObj.insertKey(5)
# heapObj.insertKey(4)
# heapObj.insertKey(45)
  
# print (heapObj.extractMin()),
# print (heapObj.getMin()),
# heapObj.decreaseKey(2, 1)
# print (heapObj.getMin())