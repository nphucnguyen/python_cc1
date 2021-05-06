BOARD_LINK = "./diem_chitiet.txt"
SAVE_LINK = "./diem_trungbinh.txt"
KHTN = ["Toan", "Ly", "Hoa", "Sinh"]
KHXH = ["Van", "Anh", "Su", "Dia"]
MON_HS2 = ["Toan", "Van", "Anh"]

class BANGDIEM:
    def __init__(self, board_link, save_link):
        self.board_link = board_link
        self.save_link = save_link
        
    def load_dulieu(self):
        with open(self.board_link) as f:
            lines = f.read().splitlines()
        tieude = lines[0].split()[1:]
        #self.rs ={}
        rs = {}
        for i in range(1,len(lines)):
            diem_chitiet = lines[i].split(";")[1:]
            rs_value = dict(zip(tieude,diem_chitiet))
            rs.update({lines[i].split(';')[0]:rs_value})
        # with open thì k cần close
        f.close()
        return rs
        
    #     if any(x in mon_n_diem for x in KHTN):

    def tinhdiem(self, dic):
        for mon, diem in dic.items():
            diem = list(map(float, diem.strip().split(",")))
            if mon in KHTN:
                dic[mon]= round(0.05*diem[0] + 0.1*diem[1] + 0.15*diem[2] + 0.7*diem[3],2)
            else: 
                dic[mon] = round(0.05*diem[0] + 0.1*diem[1] + 0.1*diem[2] + 0.15*diem[3] + 0.6*diem[4],2)
        return dic

    def tinhdiem_trungbinh(self,rs):
        for x in rs:
            rs[x] = self.tinhdiem(rs[x])
        # Hoặc
        # rs = {key: self.tinhdiem({_: item for _, item in value.items()}) for key, value in rs.items()}
        return rs

    def luudiem_trungbinh(self,rs):
        f = open(self.board_link)
        tieude = f.readline()
        f.close()
        f_write = open(self.save_link, 'w+')
        f_write.write(tieude)
        for k,v in rs.items():
            f_write.write(k+';'+';'.join(map(str,list(v.values())))+'\n')
        f_write.close()

class DANHGIA(BANGDIEM):
    #ke thua tu tinhdiem_trungbinh
    def xeploai_hocsinh(self,rs):
        rs_xeploai = rs.copy()
        def xeploai(dic):
            thuongso = 0
            tong = 0
            for k,v in dic.items():
                if k in MON_HS2:
                    tong += v*2
                    thuongso +=2
                else:
                    tong += v*1
                    thuongso +=1
            dtb_chuan = round(tong/thuongso,2)
            if all(x >=8 for x in list(dic.values())) and dtb_chuan>=9:
                return "Xuat xac"
            elif all(x >=6.5 for x in list(dic.values())) and dtb_chuan>=8:
                return "Gioi"
            elif all(x >=5 for x in list(dic.values())) and dtb_chuan>=6.5:
                return "Kha"
            elif all(x >=4.5 for x in list(dic.values())) and dtb_chuan>=6:
                return "TB Kha"
            else: return "TB"
        for k in rs_xeploai:
            rs_xeploai[k] = xeploai(rs_xeploai[k])
        return(rs_xeploai)
    def xeploai_thidaihoc_hocsinh(self,rs,khoi1,khoi2,khoi3):
        rs_khoi = rs.copy()
        khoi = list()
        for i in range(len(khoi1)):
            khoi.append(khoi1[i] + khoi2[i] +khoi3[i])
        for k in rs_khoi:
            i = 0
            rs_khoi[k] = khoi[i]
            i+=1
        return rs_khoi
class TUNHIEN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,rs):
        def khoi_tunhien(dic):
            khoiA = dic['Toan'] + dic['Ly'] + dic['Hoa']
            khoiA1 = dic['Toan'] + dic['Ly'] + dic['Anh']
            khoiB = dic['Toan'] + dic['Hoa'] + dic['Sinh']
            return [khoiA,khoiA1,khoiB]
        def xeploai_khoi(diem):
            if diem >= 24: return 1
            elif diem >=18: return 2
            elif diem >=12: return 3
            else: return 4
        rs_tunhien = list()
        for k in rs:
            rs_tunhien.append([xeploai_khoi(x) for x in khoi_tunhien(rs[k])])
        return rs_tunhien
        
class XAHOI(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,rs):
        def khoi_xahoi(dic):
            khoiC = [dic['Van'] + dic['Su'] + dic['Dia']]
            return khoiC
        def xeploai_khoi(diem):
            if diem >= 21: return 1
            elif diem >=15: return 2
            elif diem >=12: return 3
            else: return 4
        rs_xahoi = list()
        for k in rs:
            rs_xahoi.append([xeploai_khoi(x) for x in khoi_xahoi(rs[k])])
        return rs_xahoi

class COBAN (DANHGIA):
    def xeploai_thidaihoc_hocsinh(self,rs):
        def khoi_coban(dic):
            khoiD = [dic['Toan'] + dic['Van'] + dic['Anh']*2]
            return khoiD
        def xeploai_khoi(diem):
            if diem >= 32: return 1
            elif diem >=24: return 2
            elif diem >=20: return 3
            else: return 4
        rs_coban = list()
        for k in rs:
            rs_coban.append([xeploai_khoi(x) for x in khoi_coban(rs[k])])
        return rs_coban

def main():
    bang_diem = BANGDIEM(BOARD_LINK, SAVE_LINK)     
    diem_cuthe = bang_diem.load_dulieu()
    rs = bang_diem.tinhdiem_trungbinh(diem_cuthe)
    # rs = bang_diem.tinhdiem_trungbinh()
    bang_diem.luudiem_trungbinh(rs)

    danh_gia = DANHGIA(BOARD_LINK, SAVE_LINK)
    hoc_luc = danh_gia.xeploai_hocsinh(rs)

    xeploai_dh_tunhien = TUNHIEN(BOARD_LINK, SAVE_LINK)
    khoi_tunhien = xeploai_dh_tunhien.xeploai_thidaihoc_hocsinh(rs)

    xeploai_dh_xahoi = XAHOI(BOARD_LINK, SAVE_LINK)
    khoi_xahoi = xeploai_dh_xahoi.xeploai_thidaihoc_hocsinh(rs)

    xeploai_dh_coban = COBAN(BOARD_LINK, SAVE_LINK)
    khoi_coban = xeploai_dh_coban.xeploai_thidaihoc_hocsinh(rs)

    xeploai_theokhoi= danh_gia.xeploai_thidaihoc_hocsinh(rs,khoi_tunhien,khoi_xahoi,khoi_coban)
    print(xeploai_theokhoi)
    
     
if __name__ == "__main__":
    main()