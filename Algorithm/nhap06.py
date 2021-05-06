class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        # neu tim thay key trung
        for idx, element in enumerate(self.arr[h]):
            if element[0] ==key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx , kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][idx]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
t["march 6"] = 11
print(t.arr)