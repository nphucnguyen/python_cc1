# #lab3.1
# import timeit
# def binarySearch (lst,n,x):
#     l = 0; r = n-1
#     while(l<r):
#         mid = (l+r)//2
#         if lst[mid] <x:
#             l = mid +1
#         else: r = mid
#     if lst[l] == x:
#         return l
#     return -1

# @profile
# def solution(rawA,rawB):
#     a = rawA[1:]
#     n = rawA[0]
#     b = rawB[1:]
#     k = rawB[0]
#     index = []
#     for num in b:
#         index.append(binarySearch(a,n,num))
#     print(' '.join(list(map(str,index))))

# rawA = list(map(int,input("nhap day 1: ").split()))
# rawB = list(map(int,input("nhap day 2: ").split()))

# start = timeit.default_timer()
# solution(rawA,rawB)
# stop = timeit.default_timer()
# print(stop - start)

#lab3.2 Majority element : dung cay tim kiem nhi phan

def majority_element(a):
    n = len(a)
    #neu co 1 phan tu
    if n == 1:
        return a[0]
    #if khong phan tu
    if n == 0:
        return None
    
    k = n//2
    elem1 = majority_element(a[:k])
    elem2 = majority_element(a[k+1:])
    
    #Neu 2 nhanh co element giong nhau
    if elem1 == elem2:
        return elem1

    #neu 2 nhanh element khac nhau
    count1 = a.count(elem1)
    count2 = a.count(elem2)

    if count1 > k:
        return elem1
    elif count2 > k:
        return elem2
    else:
        return None

print ("Should be 1:", majority_element([2,1,0,1,1]))
print ("Should be 0:", majority_element([0,0]))
print ("Should be None:", majority_element([0,1,1,1,0,0,2]))
print ("Should be 0:", majority_element([0,1,1,1,0,0,0,0,2]))
print ("Should be None:", majority_element([0,0,1,1]))
print ("Should be None:", majority_element([0,0,1,1,2,2,1,1,2]))
print ("Should be 2:", majority_element([0,2,2,2,2,2,0,1,1]))

