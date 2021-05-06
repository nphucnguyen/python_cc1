
def xeploai_hocsinh():
    students_xeploai = {}
    for line in f:
        # x la list trong 1 dong
        x = list(map(float,line.strip().split(";")))
        x[0] = str(int(x[0]))
        dtb = ((x[1] + x[5] +x[6])*2 + x[2]+ x[3]+ x[4]+ x[7]+ x[8])/11
        if dtb>=9 and (d for d in x[1:] if d>=8):
            xep_loai = "Xuat sac"
        elif dtb>=8 and (d for d in x[1:] if d>=6.5):
            xep_loai = "Gioi"
        elif dtb>=6.5 and (d for d in x[1:] if d>=5):
            xep_loai = "Kha"
        elif dtb>=6 and (d for d in x[1:] if d>=4.5):
            xep_loai = "TB kha"
        else:   xep_loai = "TB"
        students_xeploai.update({x[0]:xep_loai})
    return (students_xeploai)

def xeploai_thidaihoc_hocsinh():
    f.seek(0)
    f.readline()
    students_xeploaithidaihoc = {}
    for line in f:
        khoithi = []
        xeploai_khoithi = []
        # x la list trong 1 dong
        x = list(map(float,line.strip().split(";")))
        x[0] = str(int(x[0]))
        khoithi.append(x[1]+x[2]+x[3])
        khoithi.append(x[1]+x[2]+x[6])
        khoithi.append(x[1]+x[3]+x[4])
        khoithi.append(x[5]+x[7]+x[8])
        khoithi.append(x[1]+x[5]+x[6]*2)
        for i in range(3):
            if khoithi[i] >=24:
                xeploai_khoithi.append(1)
            elif khoithi[i] >=18:
                xeploai_khoithi.append(2)
            elif khoithi[i] >=12:
                xeploai_khoithi.append(3)
            else:
                xeploai_khoithi.append(4)
        if khoithi[3] >=21:
            xeploai_khoithi.append(1)
        elif khoithi[3] >=15:
            xeploai_khoithi.append(2)
        elif khoithi[3] >=12:
            xeploai_khoithi.append(3)
        else:
            xeploai_khoithi.append(4)

        if khoithi[4] >=32:
            xeploai_khoithi.append(1)
        elif khoithi[4] >=24:
            xeploai_khoithi.append(2)
        elif khoithi[4] >=20:
            xeploai_khoithi.append(3)
        else:
            xeploai_khoithi.append(4)
        students_xeploaithidaihoc.update({x[0]:xeploai_khoithi})
    return(students_xeploaithidaihoc)
        
def main():
    f = open("danhgia_hocsinh.txt","w+")
    f.write("Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D")
    for k,v in xeploaithidaihoc.items():
        v1 = ";".join(list(map(str,v)))
        v2 = students_xeploai[k]
        f.write(f'\n{k};{v2};{v1}')
    f.close()


f = open("diem_trungbinh.txt")
tieude = f.readline().split()
students_xeploai = xeploai_hocsinh()
print(students_xeploai)
xeploaithidaihoc = xeploai_thidaihoc_hocsinh()
print(xeploaithidaihoc)
f.close()
main()
