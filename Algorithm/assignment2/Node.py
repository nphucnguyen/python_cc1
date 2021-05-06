class Node:
    def __init__(self,data = None):
        self.next = None
        if data is not None:
            self.data = data
            #print(data)
            self.id, self.title, self.quantity, self.price = data.strip().split()
        else:
            self.id = input('Please enter the new product ID: ')
            self.title = input("Please enter the product's name: ")
            self.quantity = input("Please enter the product's quantity: ")
            self.price = input("Please enter the product's price: ")
            self.data = ' '.join([self.id,self.title,self.quantity, self.price])
    def __str__(self):
        return self.data
    def update(self):
        self.id, self.title, self.quantity, self.price = self.data.strip().split()


    # def __str__(self):
    #     return f'{self.id} {self.title} {self.quantity} {self.price}'

