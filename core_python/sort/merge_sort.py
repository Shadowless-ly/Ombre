import time
import random


def merge(left, right):
	merged = []
	len_left = len(left)
	len_right = len(right)
	i,j = 0,0
	while (i<len_left) and (j<len_right):
		if left[i] < right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1

	merged.extend(left[i:])
	merged.extend(left[j:])
	return merged

def merge_sort(l):
	if len(l) in [1, 0]:
		return l
	middle = len(l) // 2
	left = l[:middle]
	right = l[middle:]
	return merge(merge_sort(left), merge_sort(right))


def main(l):
	print(merge_sort(l))


def rand(num):
	i = 0
	l1 = []
	while i < num:
		l1.append(random.randint(0,1000))
		i += 1
	return l1

if __name__ == '__main__':
	start = time.time()
	main(rand(5000))
	stop = time.time()
	print("start_time:%s \nstop_time :%s" %(start, stop))