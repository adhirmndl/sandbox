def sel_sort(xs):
    for i in range(len(xs)):
        for j in range(len(xs[:i])):
            if (xs[i] < xs[j]):
                tmp = xs[j]
                xs[j] = xs[i]
                xs[i] = tmp
                continue
    print xs

def bub_sort(xs):
    for i in range(len(xs))[1:]:
        for j in range(len(xs) - 1):
            if xs[i] > xs[j]:
                print xs
                tmp = xs[i]
                xs[i] = xs[j]
                xs[j] = tmp
    print xs
if __name__ == "__main__":
    sel_sort([5,4,3,2,1])
    bub_sort([5,4,3,2,1])
