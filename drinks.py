import random
DRINKS = '''1 dừa tắc - cam vắt - 68 lê hồng phong
2 tàu hủ rong biển - 124 ngô mây
3 sinh tố - 18 nguyễn huệ
4 trà sữa - 68 trần cao vân
5 rau câu dừa - nhân plan - 29 vũ bão
6 nước mía bờ biển
'''
drinks_list = DRINKS.splitlines()
random.shuffle(drinks_list)
print(*drinks_list, sep = '\n')