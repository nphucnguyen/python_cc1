import timeit



#lab 1.1 số Fibonacci bé
# def Fibonacci(n):
#     f = [0,1]
#     f.extend(f[-1]+f[-2] for i in range (2,n+1))
#     return f[n]


# n= int(input("Nhap so nguyen N: "))
# start = timeit.default_timer()
# s = Fibonacci(n)
# stop = timeit.default_timer()
# print(f'f(n) = {s}, time = {stop - start}')


#lab 1.2 chu so cuoi cua fibonacci lon
#@profile
def Fibonacci(n):
    f = [0,1]
    f.extend((f[-1]+f[-2])%10 for i in range (2,n+1))
    return f[n]


n= int(input("Nhap so nguyen N: "))
start = timeit.default_timer()
s = Fibonacci(n)
stop = timeit.default_timer()
print(f'f(n) = {s}, time = {stop - start}')
