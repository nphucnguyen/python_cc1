import random
FOODS = '''
1 Lẩu 1 người 49k – Phố đêm Quy Nhơn Nguyễn Trung Tín đến 1h sáng
2 SAMFU – Food & Chill Garden đến sáng 200k
3 Bánh xèo tôm nhảy -Các quán diên hồng
4 Ăn vặt cô Bé - Mai xuân thưởng (trứng cút, nai, chả cuốn..)

49 Quán nhậu Bốn Thu - Óc heo, má, đuôi, lòng, gà, cá , lươn, ếch, ốc 1085/19 Trần Hưng Đạo, Quy Nhơn
50 Ốc 94 Mai Xuân thưởng (ốc lên, bưu, hàu nướng) rẻDĩa ốc nhỏ đồng giá 20k/ dĩa
50a Ốc cô xí - 22 đào duy từốc ngon như ốc trộn, ốc len xào dừa, ốc hương, ốc hút, cùng với đó là những món Xìa hấp thái
50b Ốc Thúy kiều - 50 Tăng bạt hổ
50c Ốc Ngọc hân công chúa
50d Ốc Nguyễn Trãi (chỉ bán ốc bưu+ cơm rượu) - 02 Ngyễn trải
50e Ốc bưu diên hồng trần thị kỉ

51 CÁ SƠN NƯỚNG - Quán 7 DŨNG - 74A Nguyễn Hoàng, Sông bắc Hà Thanh, Quy Nhơn
52 Nghĩa Ghẹ - 19 Võ Đình Tú
53 Nem chả lợi - 113 Tăng Bạt hổ phàn 2 người 120
54 Bánh hỏi cháo lòng - 99 Ngô mây, 76A trần phú, 20 diên hồng, 22 phan bội châu
55 Bánh canh - 31 tháng 3 (2hchieu đên 5h)
56 Cháo bò ,gỏi bò 28 Trần bình trọng 30k
57 TIỆM ỐC LUỘC 35K - 318 Xuân Diệu, Quy Nhơn
58 VỊT LỘN CHIÊN MẮM - XÀO ME - ỐC ĐỦ LOẠI 345 Bạch Đằng23g
59 Gỏi ,kem gỏi Thanh Tâm - 69 Bà Triệu đến 9ruoi
60 Bún riêu bò - 102 nguyễn thái học (khuya)
60b Bún sứa- Ngọc liên 379AB NGuyễn Huệ,Quy Nhơn
60c BÚn sứa - Hồ thị 279 trần hưng đạo
60d
....
Ẩm thực trần bình trọng
ẩm thực phan bội châu (bánh canh, gỏi bò,bánh tráng, trứng tan, xèo, kem, đá me)
ẩm thực ngô văn sở (đắt)
ẩm thực ốc Ngọc hân công chúa


53 
'''
food_list = FOODS.splitlines()
random.shuffle(food_list)
print(*food_list, sep = '\n')