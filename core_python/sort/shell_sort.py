# shell sort
# -*- conding:utf-8-*-

def shellsort(l):
	# 取增量因子
	gap = len(l) // 2
	# 直到gap为1
	while gap > 0:
		# 遍历索引为gap的元素到结尾
		for i in range(gap, len(l)):
			# 当前索引大于等于gap，且当前索引i对应元素的值小于i-gap对应元素的值
			print('i' ,i, 'gap', gap, 'i-gap',i-gap)
			while (i >= gap) and l[i] < l[i - gap]:
				# 交换两个元素
				print('change:', i, '<---->', i-gap)
				l[i], l[i-gap] = l[i-gap],l[i]
				print(gap, l)
				# 
				i = i - gap
		gap = gap // 2
	return l

print(shellsort([9,8,7,6,5,4,3,2,1,0]))
