
def tinhdiem_trungbinh():
    students = {}
    for line in f:
        # x la list trong 1 dong
        x = line.strip().split(";")
        for i in range(len(x)-1):
            x[i+1] = x[i+1].split(",")
            x[i+1] = list(map(float,(y for y in x[i+1])))
        for i in range(1,5):
            x[i] = round(x[i][0]*0.05 + x[i][1]*0.1 + x[i][2]*0.15 + x[i][3]*0.7,2)
        for i in range(5,9):
            x[i] = round(x[i][0]*0.05 + x[i][1]*0.1 + x[i][2]*0.1 + x[i][3]*0.15 + x[i][4]*0.6,2)
        diem = dict(zip(tieude[1:],x[1:]))
        students.update({x[0]:diem})
    f.close()
    return students

def luudiem_trungbinh(students):
    fwrite = open("diem_trungbinh.txt", "w+")
    #Có phương thức để thao tác dễ hơn?
    for i in range(len(tieude)):
        tieude[i] = tieude[i].rjust(10)
    fwrite.write("".join(tieude))
    for x,y in students.items():
        diem = list(map(str,list(y.values())))
        for i in range(len(diem)):
            diem[i]=diem[i].rjust(9)
        diem = ";".join(diem)
        
        fwrite.write('\n' + (x+';').rjust(10) + diem)




f = open("diem_chitiet.txt")
tieude = f.readline().split()
students = tinhdiem_trungbinh()
print(students)
luudiem_trungbinh(students)

