#lab 2.1
# numCoin = 0
# indexCoin = 0
# coins = [10,5,1]
# while(True):
#     try:
#         remainder = int(input('Nhap so tien can doi: '))
#         while remainder <0 or remainder>1000:
#             print('So tien khong hop le,nhap lai: ')
#             remainder = int(input('Nhap so tien can doi: '))            
#         break
#     except:
#         print('So tien khong hop le, vui long nhap lai: ')

# while remainder>0:
#     if remainder // coins[indexCoin] >=1:
#         n = remainder // coins[indexCoin]
#         numCoin += n
#         remainder -= n*coins[indexCoin]
#     indexCoin +=1

# print('So luong dong xu la: ', numCoin)

#lab 2.2

#@profile
# def maxValue():
#     n,W = map(int,input("Nhap so luong do va trong luong tui: ").split())
#     resource = [list(map(int,input('Nhap gia tri va trong luong:').split())) for i in range(n)]
#     resource = sorted(resource, key = lambda x: x[0]/x[1], reverse= True)
#     index = 0
#     value = 0
#     while True:
#         if resource[index][1] < W:
#             W -= resource[index][1]
#             value += resource[index][0]
#             index +=1
#         else:
#             value += resource[index][0]
#             W = 0
#             break
#     return value

# value = maxValue()
# print('Tong tai san:', value)
    
#lab 2.3
# n = int(input('Nhap so vi tri: '))
# a = list(map(int,input('Nhap loi nhuan moi vi tri: ').split()))
# b = list(map(int,input('Nhap so click vi tri: ').split()))
# a = sorted(a)
# b = sorted(b)
# c = [i*j for i,j in zip(a,b)]
# print('Ket qua loi nhuan cao nhat la: ',sum(c))


#lab 2.4 thu thap chu ki
n = int(input("Nhap so doan: "))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
while len(arr)>0:
    length = len(arr)
    if length == 1:
        pass
    for i in range(length):
        arr_temp = [arr[0][0],arr[0][1],arr[i][0],arr[i][1]]
        
print(arr)

#lab 2.5
# n = int(input('Nhap so luong keo: '))
# k = 1
# listK = []
# while 2*k< n:
#     n -= k
#     listK.append(k)
#     k += 1
# listK.append(n)
# print(len(listK))
# print(' '.join(list(map(str,listK))))