import random
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wraper(*args, **kw):
        start = time.time()
        print('start time:', start)
        res = func(*args, **kw)
        stop = time.time()
        print('stop time:', stop)
        print('cost time:%f' %(stop-start))
        return res
    return wraper

def randgen(num):
    n = 0
    while n < num:
        yield random.randint(1,1000)
        n += 1

def qsort(l):
    if len(l) <= 1:
        return l
    middle = l[0]
    left = []
    right = []
    for i in l[1:]:
        if i <= middle:
            left.append(i)
        else:
            right.append(i)
    left = qsort(left)
    right = qsort(right)
    return left+[middle]+right

@timeit
def main():
    print(qsort([9,8,7,6,5,4,3,2,1]))
    

if __name__ == "__main__":
    main()
