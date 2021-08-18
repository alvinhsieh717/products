# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 繼續下一回
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#使用者購買商品名稱價格
while True:
	name = input('請輸入商品名稱:')
	if name == "q": # quit
		break
	price = input('請輸入價格:')
	price = int(price)
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	products.append([name, price]) # 簡寫法
print(products)

# 列印出商品
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')