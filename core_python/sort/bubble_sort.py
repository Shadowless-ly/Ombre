def buble_sort(l):
	if len(l) in [0, 1]:
		return l
	for i in range(len(l)-1):
		change = False
		s = 0
		for j in range(len(l)-i-1):
			if l[s] > l[s+1]:
				l[s], l[s+1] = l[s+1],l[s]
				change = True
			s += 1
		if not change:
			print('not change')
			break
	return l


def main():
	print(buble_sort([9,8,7,6,5,4,3,2,1]))


if __name__ == '__main__':
	main()