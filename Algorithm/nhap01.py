#đê qui tính giai thừa
# def Factorial (n):
#     if n<=1: return 1
#     return n*Factorial(n-1)
# n = int(input())
# print(Factorial(n))

#Đệ qui bài toán tháp Hà Nội
def ThapHN (n, A, B, C):
    if n ==1: print(f'{A} ==> {C}')
    else:
        ThapHN(n-1, A, C, B)
        print(f'{A} ==> {C}')
        ThapHN(n-1,B,A,C)

n = int(input('Nhap so luong dia: '))
ThapHN(n,'A','B','C')