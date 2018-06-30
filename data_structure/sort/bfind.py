def bfind(data, target):
    head = 0
    tail = len(data)-1
    while head <= tail:
        mid = (head + tail) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            head = mid + 1
        else:
            tail = mid - 1
    return False


def find(head, tail, data, target):
    if head > tail:
        return False
    mid = (head + tail) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        head = mid + 1
    else:
        tail = mid - 1
    return find(head, tail ,data, target)

print(bfind(range(100000), 1110000))
print(find(0, len(range(10000))-1 ,range(10000), 1001))


