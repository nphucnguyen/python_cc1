#Mục tiêu: đoạn văn bản được xử lí bỏ dấu . , tạo list các từ
name = input("Enter File name: ")
handle = open(name)

counts = dict()
for line in handle:
	#Bỏ dấu chấm cuối câu
	line = line.strip('.')
	#bỏ dấu chấm giữa câu
	line = line.replace('. ', ' ')
	#bỏ dấu , giữa câu
	line = line.replace(', ',' ')
	#phân tách thành list
	words = line.split()

	#Thêm vào danh sách dictionaries
	for word in words:
		counts[word] = counts.get(word,0) + 1
print(counts)

maxword = None
maxcount = None
for word, count in counts.items():
	if maxcount is None or count > maxcount:
		maxword = word
		maxcount = count
print(maxword, maxcount)

