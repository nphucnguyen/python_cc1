# #4.1
# n = int(input('Nhap so n: '))
# paces = [0] * n
# for i in range(1,n):
#     pace_x2 = paces[(i+1)//2-1] +1
#     pace_x3 = paces[(i+1)//3-1] +1
#     pace_plus1 = paces[i-1] +1
#     if (i+1)%3== 0 and (i+1) %2 == 0:
#         paces[i] = min(pace_x2,pace_x3,pace_plus1)
#     elif (i+1)%3 == 0:
#         paces[i] = min(pace_x3,pace_plus1)
#     elif (i+1) %2 == 0:
#         paces[i] = min(pace_x2,pace_plus1)
#     else:
#         paces[i] = pace_plus1
#     # if (i+1)%3 ==0 :
#     #     j = (i+1)/3 -1
#     #     paces[i] = paces[j]+1
# temp = paces[-1]-1
# a= n
# number = []
# for i in range(n-1,0,-1):
#     if paces[i] == temp:
#         if a/3 == i+1:
#             number.insert(0,i+1)
#             a /=3
#             temp= temp -1
#         elif a/2 ==i +1:
#             number.insert(0,i+1)
#             a /=2
#             temp = temp -1
#         elif a-1 == i+1:
#             number.insert(0,i+1)
#             a -=1
#             temp = temp -1
# number.insert(0,1)
# number.append(n)
# print(paces[-1])
# print(number)

#4.2 Maximum amount of gold
def get_gold(W, golds):
    ar = [None] *(W+1)
    ar[0] = golds
    for i in range(1,W+1):
        for x in golds:
            if x <=i and ar[i-x]:
                if x in ar[i-x]:
                    ar[i] = ar[i-x].copy()
                    ar[i].remove(x)
                    break
    index = W
    while ar[index] == None:
        index -=1
    return index
W = 10
golds = [1, 4, 8]
print(get_gold(W, golds))
'''

'''

