def get_next(T):
    i = 1
    j = 0
    nxt=dict()
    nxt[1] = 0
    while i < len(T):
        if (j == 0 or T[i] == T[j-1]):
            i+=1
            j+=1
            nxt[i] = j
        else:
            j = nxt[j]
    return nxt

if __name__ == "__main__":
    print(get_next("ababcd"))