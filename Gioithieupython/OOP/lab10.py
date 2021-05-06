
#lab 10.1
# class Student:
#     def __init__ (self, student_name = '', diemtb = ''):
#         self.name = student_name
#         self.diemtb = diemtb
#     def print_diemtk(self, diemtb):
#         self.diemtb = sum(map(float,diemtb.strip().split()))/len(diemtb.strip().split())
#         print(f"The averall mark of {self.name} is {self.diemtb}")

# student = Student()
# student.name = input("Nhap ten: ")
# student.print_diemtk(input("Nhap cac diem: "))

#lab 10.2
# class NhanVien:
#     def __init__ (self,name='', thong_tin = ''):
#         self.name = name
#         self.thang, self.luongcoban, self.ngaylamviec, self.hesoluong = map(float,thong_tin.strip().split())
#     def tinhluong(self):
#         luongtong = self.luongcoban * self.ngaylamviec * self.hesoluong - 1000000
#         if luongtong > 9000000:
#             luong_thucnhan = 0.9 * luongtong
#             return luong_thucnhan
#         else:
#             luong_thucnhan = luongtong
#             return luong_thucnhan
#     def hienthiluong(self):
#         print(f'Luong cua nhan vien {self.name} nhan duoc trong thang {self.thang} la: {self.tinhluong()}')

# ten_nhan_vien = input("Nhap ten nhan vien: ")
# thong_tin = input("Nhap thong tin luong: ")
# nv  = NhanVien(ten_nhan_vien, thong_tin)
# nv.hienthiluong()


#lab 10.3
class NhanVien:
    def __init__ (self,name ,thang , luongcoban, ngaylamviec, hesoluongVana):
        self.name = name
        self.thang = thang
        self.luongcoban = luongcoban
        self.ngaylamviec = ngaylamviec
        self.hesoluong = hesoluong
    def tinhluong(self):
        luongtong = self.luongcoban * self.ngaylamviec * self.hesoluong - 1000000
        if luongtong > 9000000:
            luong_thucnhan = int(0.9 * luongtong)
            return luong_thucnhan
        else:
            luong_thucnhan = int(luongtong)
            return luong_thucnhan
    def hienthiluong(self):
        print(f'Luong cua nhan vien {self.name} nhan duoc trong thang {self.thang} la: {self.tinhluong()}')

class QuanLi(NhanVien):
    def __init__ (self, name , thang, luongcoban, ngaylamviec, hesoluong, performance):
        super().__init__ (name, thang, luongcoban, ngaylamviec, hesoluong)
        self.hesothuong = performance
    
    def tinhluong(self):
        luongtong_chuathuong = self.luongcoban * self.ngaylamviec * self.hesoluong - 1000000
        if luongtong_chuathuong > 9000000:
            luongnhan_chuathuong = 0.9 * luongtong_chuathuong
        else:
            luongnhan_chuathuong = luongtong_chuathuong
        if self.hesothuong < 1:
            luong_thucnhan = luongnhan_chuathuong * self.hesothuong
            return int(luong_thucnhan)
        else:
            luong_thuong = luongtong_chuathuong * (self.hesothuong -1 ) * 0.85
            luong_thucnhan = luongnhan_chuathuong + luong_thuong
            return int(luong_thucnhan)

# ten_quanli = input("Nhap ten nhan vien: ")
# thong_tin = map(float,input("Nhap thong tin luong: ").strip().split())
# ql  = QuanLi(ten_quanli, *thong_tin)
# ql.hienthiluong()

nv1 = NhanVien ("nguyen",3, 200000, 22, 1.5)
print(nv1.tinhluong())
