import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wraper(*args, **kw):
        start = time.time()
        print('start time:', start)
        result = func(*args, **kw)
        stop = time.time()
        print('stop time:', stop)
        print('cost time: %f' %(stop-start))
        return result
    return wraper

def merge(left, right):
    if len(left)<0 or len(right)<0:
        return left or right
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(left[j:])
    return merged

def mergesort(l):
    if len(l) <= 1:
        return l
    middle = len(l) // 2
    return merge(mergesort(l[:middle]),mergesort(l[middle:]))
@timeit
def main():
    print(mergesort([9,8,7,6,5,4,3,2,1]))

if __name__ == "__main__":
    main()
