class Student():
    def __init__(self,student_fullname, diemtb):
        self.fullname = student_fullname    #có thể đổi sau khi khai báo, nhung k nên
        self.diemtb = sum(map(float,diemtb.strip().split()))/len(diemtb.strip().split())
    @property   #biến method thành attribute, đây là getter
    def familyname(self):
        return self.fullname.split()[0]
    # @property
    # def fullname(self):
    #     return self.fullname

    def name(self): # vẫn là method
        return " ".join(self.fullname.split()[1:])

    #Muốn đổi họ tên mới thì nên thêm kiểu vầy, đây là setter, nhưng trước khi có setter phải có getter fullname
    @fullname.setter
    def fullname(self, new_fullname):
        self.fullname = new_fullname
        self.familyname = new_fullname.split()[0]
        self.name = new_fullname.split()[1:]

    

    

student_A = Student(input("Nhap ho va ten: "),input("Nhap diem cac mon: "))
print(student_A.fullname)
print(student_A.diemtb)


