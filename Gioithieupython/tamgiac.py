import math

def nhap_toa_do ():
  while True:
      try:
          a = float(input("Nhap toa do: "))
          break
      except:
          print("Khong phai la so thuc. Vui long nhap lai")          
  return a

def kiemtra_tamgiac(a):
  if a[3] - a[1] == 0 and a[5] - a[1] == 0 :
    return False
  elif a[3] - a[1] == 0 or a[5] - a[1] == 0 :
    return True
  elif (a[2]-a[0])/(a[3]-a[1]) == (a[4]-a[0])/(a[5]-a[1]):
    return False
  else:
    return True

def goccanh_tamgiac(t):
    

  AB = math.sqrt((t[2]-t[0])**2 + (t[3]-t[1])**2)
  BC = math.sqrt((t[4]-t[2])**2 + (t[5]-t[3])**2)
  AC = math.sqrt((t[4]-t[0])**2 + (t[5]-t[1])**2)


  gocA = math.acos((AC**2 + AB **2 - BC**2)/(2*AC*AB))
  gocB = math.acos((BC**2 + AB **2 - AC**2)/(2*BC*AB))
  gocC = math.acos((AC**2 + BC **2 - AB**2)/(2*AC*BC))
  lst_goccanh_tamgiac = [AB,BC,AC,gocA,gocB,gocC]
  return lst_goccanh_tamgiac

def xet_tamgiac(g):

    if g[0] == g[1] and g[1] == g[2]:
        return "ABC la tam giac deu."
    elif g[0] == g[2]:
        if g[3] == round(math.pi/2,2):
            return 'ABC la tam giac vuong can tai dinh A'
        elif g[3] > round(math.pi/2,2):
            return 'ABC la tam giac tu va can tai dinh A'
        else:
            return 'ABC la tam giac nhon va can tai dinh A'
    elif g[0] == g[1]:
        if g[4] == round(math.pi/2,2):
            return 'ABC la tam giac vuong can tai dinh B'
        elif g[4] > round(math.pi/2,2):
            return 'ABC la tam giac tu va can tai dinh B'
        else:
            return 'ABC la tam giac nhon va can tai dinh B'
    elif g[2] == g[1]:
        if g[5] == round(math.pi/2,2):
            return 'ABC la tam giac vuong can tai dinh C'
        elif g[5] > round(math.pi/2,2):
            return 'ABC la tam giac tu va can tai dinh C'
        else:
            return 'ABC la tam giac nhon va can tai dinh C'
    else:
        if g[3] == round(math.pi/2,2):
            return 'ABC la tam giac vuong tai dinh A'
        if g[4] == round(math.pi/2,2):
            return 'ABC la tam giac vuong tai dinh B'
        if g[5] == round(math.pi/2,2):
            return 'ABC la tam giac vuong tai dinh C'
        if g[3] > round(math.pi/2,2):
            return 'ABC la tam giac tu tai dinh A'
        if g[4] > round(math.pi/2,2):
            return 'ABC la tam giac tu tai dinh B'
        if g[5] > round(math.pi/2,2):
            return 'ABC la tam giac tu tai dinh C'
        return 'ABC la tam giac nhon'
      
def dientich_tamgiac(g):
    p = (g[0] + g[1] + g[2])/2
    s = math.sqrt(p*(p-g[0])*(p-g[1])*(p-g[2]))   
    return s

def duongcao_tamgiac(g,s):
    dcA = 2*s/g[1]
    dcB = 2*s/g[2]
    dcC = 2*s/g[0]
    dc = [dcA,dcB,dcC]
    return dc

def tam_tamgiac(t):
    trongtamx = (t[0] + t[2] + t[4])/3
    trongtamy = (t[1] + t[3] + t[5])/3
    trongtam = [trongtamx,trongtamy]
    return trongtam

def trungtuyen_tamgiac(t,tt):
    tB = math.sqrt((t[2]-tt[0])**2 + (t[3]-tt[1])**2)
    tC = math.sqrt((t[4]-tt[0])**2 + (t[5]-tt[1])**2)
    tA = math.sqrt((t[0]-tt[0])**2 + (t[1]-tt[1])**2)
    tt = [tA,tB,tC]
    return tt
    
def giaima_tamgiac(T):
    if kiemtra_tamgiac(T) is True:
        print("A, B, C hop thanh mot tam giac")
    else:
        print("A, B, C khong hop thanh mot tam giac")
        quit()



    
    

print("Nhap toa do cac diem trong tam giac: ")
T = []
for diem in range(6):
  T.append(nhap_toa_do())
  #Toa do Ax, Ay
print (T)

giaima_tamgiac(T)
  

goccanh = goccanh_tamgiac(T)
goccanh_round = [round(ele,2) for ele in goccanh]
print("Chieu dai canh AB:",goccanh_round[0])
print("Chieu dai canh BC:",goccanh_round[1])
print("Chieu dai canh CA:",goccanh_round[2])
print("Goc A:",goccanh_round[3])
print("Goc B:",goccanh_round[4])
print("Goc C:",goccanh_round[5])

print(xet_tamgiac(goccanh_round))

dientich = dientich_tamgiac(goccanh)
print("Dien tich: ",round(dientich,2))

dc = duongcao_tamgiac(goccanh,dientich)
dc_round = [round(ele,2) for ele in dc]
print('Do dai duong cao tu dinh A:', dc_round[0])
print('Do dai duong cao tu dinh B:', dc_round[1])
print('Do dai duong cao tu dinh C:', dc_round[2])

trongtam = tam_tamgiac(T)
trongtam_round = [round(ele,2) for ele in trongtam]
print("Toa do trong tam:", trongtam_round)

trungtuyen = trungtuyen_tamgiac(T,trongtam)
trungtuyen_round = [round(ele,2) for ele in trungtuyen]
print('Khoang cach den trong tam tu dinh A:',trungtuyen_round[0])
print('Khoang cach den trong tam tu dinh B:',trungtuyen_round[1])
print('Khoang cach den trong tam tu dinh C:',trungtuyen_round[2])
