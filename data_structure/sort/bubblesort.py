import quicksort

def bubble(l):
    if len(l) <= 1:
        return l
    for i in range(len(l)-1):
        change = 0
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                change = 1
        if change == 0:
            break
    return l

@quicksort.timeit
def main():
    print(bubble([9,8,7,6,5,4,3,2,1]))

if __name__ == "__main__":
    main()
