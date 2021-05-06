#tạo lóp danh sách sinh viên
class Student:
    #Danh sách attribute
    id = ''
    name = ''

    #construtor method là hàm đặc biệt, dc gọi tự động mỗi khi tạo mới 1 instance object
    #khi goi ham thi bat buoc phai them tham so truyen vao
    def __init__ (self,id, name):
        self.id = id
        self.name = name
    #methods
        #add student
    def add(self,id,name):
        print("add student")
        self.id = id
        self.name = name
        #show method
    def show(self):
        print("show student")
        print(f"id: {self.id}, name: {self.name}")
    #static method:có thể dc gọi mà k cần tạo instance object
    @staticmethod
    def add2numbers (a,b):
        return a+b
#s chinh la 1 instance object
#buoc phải thêm tham số truyền vào hàm khởi tạo vì có __init__
s = Student(input(),input())
s.show()

#ở trên là cách khởi tạo thông thường, còn 1 cách khởi tạo nữa, tiện lợi hơn với 1 dòng, đòi hỏi cần có constructors method
#staticmethod
print(Student.add2numbers(3,4))

#Lớp con có thể kế thừa các thuộc tính và phương thức của lớp cha, trừ trường hợp đó là một private method


