'''
BOARD_LINK = "./diem_chitiet.txt"
SAVE_LINK = "./diem_trungbinh.txt"
KHTN = ["Toan", "Ly", "Hoa", "Sinh"]
KHXH = ["Van", "Anh", "Su", "Dia"]
MON_HS2 = ["Toan", "Van", "Anh"]

class BANGDIEM:
    def __init__(self, board_link, save_link):
        self.board_link = board_link
        self.save_link = save_link
    def load_dulieu(self):
        with open(self.board_link) as f:
            lines = f.read().splitlines()
        tieude = lines[0].split()[1:]
        #self.rs ={}
        rs = {}
        for i in range(1,len(lines)):
            diem_chitiet = lines[i].split(";")[1:]
            rs_value = dict(zip(tieude,diem_chitiet))
            rs.update({lines[i].split(';')[0]:rs_value})
        # with open thì k cần close
        f.close()
        return rs

'''
import os
BOARD_LINK = './INPUT.TXT'      
SAVE_LINK_1 = './OUTPUT1.TXT'   #bubble sort
SAVE_LINK_2 = './OUTPUT2.TXT'   # selection sort
SAVE_LINK_3 = './OUTPUT3.TXT'   # insert sort
SAVE_LINK_4 = './OUTPUT4.TXT'   # linear search
SAVE_LINK_5 = './OUTPUT5.TXT'   # binary search

'''
1.def cho menu
    a.Nhap du lieu cho ban phim
    Nhập giá trị n
VD về output: 9 3 5 6 1 2 4
    ...



'''

class sort:
    def __init__(self):
        self.n = None
        self.data = None
    def option(self):
        x = input('Please enter the choice: ')
        if x == '1': self.manual_input()
        elif x == '2': self.load()
        elif x == '3': self.bubbleSort()
        elif x == '4': self.selectionSort()
        elif x == '5': self.insertionSort()
        elif x == '6': self.linearSearch()
        elif x == '7': self.binarySearch()
        elif x == '0':
            print('Thanks!!!')
            return
        else:
            print('No option, please enter a choice again: ')
        # back to menu
        self.menu()
        


    def menu(self):
        MENU ='''
        +-----------Menu------------+
        |   1.Manual Input          |
        |   2.File Input            |
        |   3.Bubble sort           |
        |   4.Selection sort        |
        |   5.Insertion sort        |
        |   6.Linear search         |
        |   7.Binary search         |
        |   0.Exit                  |    
        '''
        print(MENU)
        self.option()

    def manual_input(self):
        with open(BOARD_LINK,'w') as f:
            f.writelines([input('Please enter input number of elements: '),'\n'])
            f.write(input('Please enter input elements: '))
    def load(self):
        with open(input('Please enter the file path: ')) as f:
            self.n = int(f.readline().strip())
            data = f.readline()
            print(data)
            self.data = list(map(float,data.strip().split()))
    def bubbleSort(self):
        with open(SAVE_LINK_1,'w') as f:
            ar = self.data.copy()
            n = len(ar)
            # pp nhỏ nổi trước (duyệt ngược chiều)
            for i in range(n):
                for j in range(n-1,i,-1):
                    if ar[j-1]>ar[j]: ar[j-1] , ar[j] = ar[j] , ar[j-1]
                print(ar)
                print(ar,file=f)
            return ar

    def selectionSort(self):
        with open(SAVE_LINK_2,'w') as f:
            ar = self.data.copy()
            n = len(ar)
            for i in range(n-1):
                min = i
                for j in range(i+1,n):
                    if ar[i]>ar[j]: min = j
                ar[i], ar[min] = ar[min], ar[i]
                print(ar)
                print(ar,file = f)


    def insertionSort(self):
        with open(SAVE_LINK_3,'w') as f:
            ar = self.data.copy()
            n = len(ar)
            for i in range(1,n):
                for pos in range(i,0,-1):
                    if ar[pos-1] > ar[pos]: ar[pos-1] , ar[pos] = ar[pos] , ar[pos-1]
                print(ar)
                print(ar,file = f)
    #above the chosen value
    def linearSearch(self):
        with open(SAVE_LINK_4,'w') as f:
            value = float(input('Please enter searched input value: '))
            print(value)
            ar = self.data.copy()
            print(ar)
            n = len(ar)
            position = []
            for i in range(n):
                if ar[i] > value:
                    position.append(str(i))
            position_str = ' '.join(position)
            print(f'Larger position: {position_str}')
            print(position_str,file= f)

        
    def binarySearch(self):
        x=float(input('Please enter the looking number: '))
        ar = self.bubbleSort().copy()
        n = len(ar)
        l = 0; r = n -1
        while(l<r):
            mid = (l+r)//2
            if ar[mid] <x:
                l = mid +1
            else: r = mid
        if ar[l] == x:
            print(f'The first position: {l}')
        else:
            print('The number is not on the list')
    



    
    






lst = sort()
lst.menu()



