BOARD_LINK = "./diem_chitiet.txt"
SAVE_LINK = "./diem_chitiet_save.txt"
KHTN = ["Toan", "Ly", "Hoa", "Sinh"]
KHXH = ["Van", "Anh", "Su", "Dia"]

class BANGDIEM:
    def __init__(self, board_link, save_link):
        self.board_link = board_link
        self.save_link = save_link
        
    def load_dulieu(self):
        with open(self.board_link) as f:
            lines = f.read().splitlines()
        rs = []
        for i in range(1,len(lines)):
            rs.append(list(map(lambda x, y: x+ ':' +y, lines[0].split(), \
            lines[i].split(";"))))
        return rs

    def tinhdiem_theomon(self, mon_n_diem):
        diem_ls = mon_n_diem.strip().split(":")[-1].split(",")
        diem_ls = list(map(float, diem_ls))
        if any(ext in mon_n_diem for ext in KHTN):
            diem_tb = 0.05*diem_ls[0] + 0.1*diem_ls[1] + 0.15*diem_ls[2] + \
            0.7*diem_ls[3]
        else:
            diem_tb = 0.05*diem_ls[0] + 0.1*diem_ls[1] + 0.1*diem_ls[2] + \
            0.15*diem_ls[3] + 0.6*diem_ls[4]
        ketqua = mon_n_diem.strip().split(":")[0]  + ": " + str(round(diem_tb, 2))
        return ketqua

    def tinhdiem_trungbinh(self,rs):
        print(rs)
        # for x in rs:
        #     print(rs[x])

        # diem_tb_rs = list()
        # while id < len(rs):
        #     hoc_sinh = rs[id][1:]
        #     diem_tb_list = list(map(lambda x: self.tinhdiem_theomon(x), hoc_sinh))
        #     diem_tb_rs.append(diem_tb_list)
        #     id+=1
        # return diem_tb_rs 



if __name__ == "__main__":
    bang_diem = BANGDIEM(BOARD_LINK, SAVE_LINK)     
    lines = bang_diem.load_dulieu()
    bang_diem.tinhdiem_trungbinh(lines)

    #rs = bang_diem.tinhdiem_trungbinh()
    #print(rs)   