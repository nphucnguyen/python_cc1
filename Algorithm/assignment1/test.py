def Bubblesort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]: a[j-1] , a[j] = a[j] , a[j-1]
    return a
a = [8,4,6,2,9,10,23,1]
print(Bubblesort(a))