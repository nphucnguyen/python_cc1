import random

# def Bubblesort(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(n-1,i,-1):
#             if a[j-1]>a[j]: a[j-1] , a[j] = a[j] , a[j-1]
#     return a

# def Selectionsort(a):
#     n = len(a)
#     for i in range(n-1):
#         min = i
#         for j in range(i+1,n):
#             if a[i]>a[j]: min = j
#         a[i], a[min] = a[min], a[i]
#     return a

# def Insertionsort(a):
#     n = len(a)
#     for i in range(1,n):
#         for pos in range(i,0,-1):
#             if a[pos-1] > a[pos]: a[pos-1] , a[pos] = a[pos] , a[pos-1]
#     return a


# def Interchangesort(a):
#     n = len(a)
#     for i in range (n-1):
#         for j in range(i,n):
#             if a[i] > a[j]: a[i],a[j] = a[j],a[i]
#     return a


# #Merge sort
# from memory_profiler import profile
# #@profile
# def Merge(a,left, mid, right):
#     temp = [0]*(right-left+1)
#     pos = 0
#     i = left
#     j = mid +1
#     while i <=mid and j <=right:
#         if a[i] < a[j]:
#             temp[pos] = a[i]
#             pos +=1; i+=1
#         else:
#             temp[pos] = a[j]
#             pos +=1; j+=1
#     while i<=mid and j>right:
#         temp[pos] = a[i]
#         pos +=1; i+=1
#     while i>mid and j<=right:
#         temp[pos] = a[j]
#         pos +=1; j+=1

#     for k in range(len(temp)):
#         a[left + k] = temp[k]

# def Mergesort(a,left,right):
#     if left >=right: return
#     mid = (left + right)//2
#     Mergesort(a,left,mid)
#     Mergesort(a,mid+1,right)
#     Merge(a,left,mid,right)
#     return a
# a = [random.randrange(1,10,1) for i in range(15)]
# print(a)
# n = len(a)
# print(Mergesort(a,0,n-1))


#shell sort
def shellSort(ar):
    n = len(ar)
    gap = n//2
    while gap >0:
        for i in range(gap,n):
            # con so chen vao day~ da xap xep truoc
            anchor = ar[i]
            j = i
        #left
            while j >=gap and ar[j-gap] >anchor:
                ar[j] = ar[j-gap]
                j -= gap
            ar[j] = anchor
        gap = gap//2
    return ar

ar = [21,38,29,17,4,25,11,32,9]
print(shellSort(ar))