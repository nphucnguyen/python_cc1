#car fueling problem
# def minRefills(x,n,L):
#     numRefills = 0; currentRefill = 0
#     while currentRefill <=n:
#         lastRefill = currentRefill
#         while(currentRefill<=n and x[currentRefill+1]-x[lastRefill]<=L):
#             currentRefill +=1
#         if currentRefill == lastRefill:
#             return 'Impossible'
#         if currentRefill <=n:
#             numRefills +=1
#     return numRefills

# L = int(input('Nhap full tank: '))
# n = int(input('Nhap so luong tram xang giua duong: '))
# x = [int(input('Nhap cac diem dung chan:')) for i in range(n+2)]

# print(minRefills(x,n,L))


#Fractional knapsack
