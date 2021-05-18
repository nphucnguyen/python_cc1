class Node:
    def __init__(self,ID,Name,DayofBirth,Birthplace):
        self.id = ID
        self.name = Name
        self.birthDay = DayofBirth
        self.birthPlace = Birthplace
        self.left = None
        self.right = None
    def __str__(self):
        return f'{self.id} {self.name} {self.birthDay} {self.birthPlace}'     
