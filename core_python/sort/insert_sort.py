def insert_sort(l):

	# 列表总长
	length = len(l)

	# 从第二个元素开始比较
	for now in range(1, length):
		# 已将排序好的元素
		ready = now - 1
		# 如果当前元素小于已经排序好的元素
		if l[now] < l[ready]:
			# 将当前值暂存
			temp = l[now]
			# 当对比的已排序值直到首个元素且当前元素均小于已排序元素
			while ready >= 0 and temp < l[ready]:
				# 已比较元素向左移动
				l[ready+1] = l[ready]
				# 继续比较右边元素
				ready -= 1
		l[ready+1] = temp
	return l
	

def main():
	print(insert_sort([9,8,7,6,5,4,3,2,1,0]))

if __name__ == '__main__':
	main()




		
