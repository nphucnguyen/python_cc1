def Euclid(a,b):
    if b==0:
        return a
    elif a%b == 0:
        return b  
    else:
        remain = a%b
        return Euclid(b,remain)


print(Euclid(3918848,1653264))