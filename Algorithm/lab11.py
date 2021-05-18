#11.1 Quan li danh bạ điện thoại
# method: add, del, find
# input : n dòng: add 911 police
# find 76213
# del 911
# output: not found
#
class ListNode:
    def __init__(self, phone_num, name):
        self.pair = (phone_num, name)
        self.next = None

class MyHashMap:

    def __init__(self):
        #setup array
        self.m = 1000
        self.h = [None]*self.m
        

    def add(self, phone_num, name):
        """
        value will always be non-negative.
        :type phone_num: int
        :type value: int
        :rtype: void
        """
        index = phone_num % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(phone_num, name)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == phone_num:
                    cur.pair = (phone_num, name) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(phone_num, name)
        

    def get(self, phone_num):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = phone_num % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == phone_num:
                return cur.pair[1]
            else:
                cur = cur.next
        return 'not found'
            
        

    def remove(self, phone_num):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = phone_num % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == phone_num:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == phone_num:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
                


# Your MyHashMap object will be instantiated and called as such:
phonebook = MyHashMap()
phonebook.add(911,'police')
phonebook.add(76213,'Mom')
phonebook.add(17239,'Bob')
phonebook.add(76213,'daddy')
print(phonebook.get(76213))
phonebook.remove(76213)
print(phonebook.get(76213))





#lab11.2:
# '''
# method: add,del,find, check
#     find: xuat yes hoac no
#     check i: xuat noi dung của list thứ i trong bảng
#     chèn vào hash thì chèn vào đầu chain

# '''

# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.next = None
# class StrHash:
#     def __init__(self,bucket):
#         self.maxsize = bucket
#         self.h = [None] * self.maxsize
#     def _hash_function_index(self,word):
#         p = 1000000007
#         x = 263
#         temp_num = 0
#         n = len(word)
#         for i in range(n):
#             temp_num += ord(word[i]) * (x**i)
#         index = (temp_num % p) % self.maxsize
#         return index
#     def add (self,data):
#         index = self._hash_function_index(data)
#         if self.h[index] is None:
#             self.h[index] = data
#         else:
#             self.h[index] = data + ' ' + self.h[index]
#     def find(self,data):
#         index = self._hash_function_index(data)
#         if self.h[index] is None:
#             print ('No')
#         else:
#             arr = self.h[index].strip().split()
#             if data in arr:
#                 print('Yes')
#             else:
#                 print('No')
#     def check(self,index):
#         print(self.h[index])
#     def Del (self,data):
#         index = self._hash_function_index(data)
#         if self.h[index] is None:
#             return
#         else:
#             self.h[index] = self.h[index].replace(data,'')

# strHash = StrHash(5)
# strHash.add('world')
# strHash.add('HellO')
# strHash.check(4)
# strHash.find('World')
# strHash.find('world')
# strHash.Del('world')
# strHash.check(4)





#thuat toan Rabin - Karp
# #lab 11.3
# #tim cac index xuat hien cua cum tu cu the so voi doan van ban lon

# x =10
# p = 255
# def search(patten, txt):
#     # q is prime number
#     m = len(patten)
#     n = len(txt)
#     pat_value = 0   # hash value for pattern
#     txt_value = 0   # hash value for txt
#     result = []
#     for i in range(m):
#         pat_value += ord(patten[i]) * (x**(m-i-1))
#         txt_value += ord(txt[i]) * (x**(m-i-1))
#     pat_value = pat_value % p
#     txt_value = txt_value % p
#     for index in range(n-m+1):
#         if pat_value == txt_value:
#             if patten == txt[index:index+m]:
#                 result.append(index)
#         else:
#             txt_value = (((txt_value - ord(txt[index])*((x**(m-1))%p))*x)%p +ord(txt[index+m]))%p
#     return result

# txt = 'geeksgeeks'
# patten = 'geek'
# print(search(patten,txt))

