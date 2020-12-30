from animate import Plot

def cmp(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    return -1


def insertsort(L, left, right, cmpfunc = cmp):
    for i in range(left+1, right+1):   # L[left] jest posortowany
        item = L[i]
        j = i
        while cmpfunc(j, left) == 1 and cmp(L[j-1], item) == 1:
            L[j] = L[j-1]   # robimy miejsce na item
            j = j-1
        L[j] = item
        Plot(i+1, L)
    return L