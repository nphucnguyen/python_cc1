# min heap (root is min)
from heapq import heapify, heappop, heappush
#heappop : pop and return smallest element
#heapify: turn arr to heap data

class Minheap:
    def __init__(self):
        self.heap = []
    def parent(self,i):
        return (i-1)/2
    def insertKey(self,k):
        heappush(self.heap,k)
    #Decrease value of key at index i to new value
    def decreaseKey(self, i , new_val):
        self.heap[i] = new_val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i] , self.heap[self.parent(i)] = (
                self.heap[self.parent(i)] , self.heap[i]
            )
    def extractMin(self):
        return heappop(self.heap)
    def deleteKey(self,i):
        self.decreaseKey(i, float('-inf'))
        self.extractMin()
    def getMin(self):
        return self.heap[0]


arr = [10, 4, 5, 1, 7, 9]
