    
def Quicksort(a,l,r):
    if l >= r: return
    m = (l+r)//2
    temp_left = []
    temp_right = []
    temp_mid = []
    len_left = 0
    length = 0
    len_right = 0
    for i in range(l,r+1):
        if a[i] < a[m]:
            temp_left.append(a[i])
            len_left +=1
        elif a[i] == a[m]:
            temp_mid.append(a[i])
            length +=1
        else:
            temp_right.append(a[i])
            len_right +=1
    temp = temp_left +temp_mid +temp_right
    for i in range(l,r+1):
        a[i] = temp[i-l]
    Quicksort(a,l,len_left-1)
    Quicksort(a,l+len_left+length,r)
    return a

a = [2,3,9,2,2,13,13,24,26,2,2,2,2,1,1,17]
right = len(a)-1
Quicksort(a,0,right)
print(a)



        