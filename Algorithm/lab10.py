#lab10.1 tao minheap tu arr
import sys
class Minheap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        # self.Heap = [float('inf')]*(self.maxsize )
        self.Heap = []
    def parent(self,pos):
        return (pos-1)//2
    def leftChild(self,pos):
        return 2*pos +1
    def rightChild(self,pos):
        return 2*pos +2
    def swap(self,pos1,pos2):
        self.Heap[pos1] , self.Heap[pos2] = self.Heap[pos2] , self.Heap[pos1]
    def insert(self,ele):
        if self.size >= self.maxsize:
            return
        #self.Heap[self.size] = ele
        self.Heap.append(ele)
        self.size +=1
        # if self.size ==1:
        #     return
        cur = self.size -1
        while self.Heap[cur] < self.Heap[self.parent(cur)]:
            self.swap(cur , self.parent(cur))
    def insert_arr(self,arr):
        n = len(arr)
        self.Heap.extend(arr)
        self.size += n
    def remove(self):
        popped = self.Heap[0]
        self.Heap[0] = self.Heap[self.size -1]
        self.size -=1
        self.minHeapify(0)
        return popped
    def minHeap(self):
        for pos in range((self.size -2)//2, -1 , -1):
            self.minHeapify(pos)
    def isLeaf(self,pos):
        if pos < self.size and pos >= (self.size+1)//2:
            return True
        return False
    def __str__(self):
        return str(self.Heap)
    def minHeapify(self, pos):
        leftChild = self.leftChild(pos)
        rightChild = self.rightChild(pos)
        if not self.isLeaf(pos):
            if rightChild >= self.maxsize:
                if self.Heap[pos] > self.Heap[leftChild]:
                    self.swap(pos, leftChild)
                    print('{} {}'.format(pos,leftChild))
                    self.minHeapify(leftChild)
            else:
                if self.Heap[pos] > self.Heap[leftChild] or \
                    self.Heap[pos] > self.Heap[rightChild]:
                    if self.Heap[leftChild] < self.Heap[rightChild]:
                        self.swap(pos,leftChild)
                        print('{} {}'.format(pos,leftChild))
                        self.minHeapify(leftChild)
                    else:
                        self.swap(pos,rightChild)
                        print('{} {}'.format(pos,rightChild))
                        self.minHeapify(rightChild)
                    

mi = Minheap(15)
# mi.insert(5)
# mi.insert(3)
# mi.insert(17)
# mi.insert(10)
# mi.insert(84)
# mi.insert(19)
# mi.insert(6)
# mi.insert(22)
# mi.insert(9)
arr = [5,4,3,2,1]
mi.insert_arr(arr)
mi.minHeap()

print(mi)

#lab10.2 xu li song song
