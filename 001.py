# import time
# start_time = time.time()


# end_time = time.time()
# print(end_time-start_time)

@profile
def append_lst():
    lst=[]
    for i in range(10000):
        lst.append(i)
append_lst()