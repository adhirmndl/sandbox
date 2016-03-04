def selection_sort(xs):
    for i in range(len(xs))[1:]:
        #print xs
        for j in range(i+1):
            if xs[i] < xs[j]:
                tmp   = xs[i]
                xs[i] = xs[j]
                xs[j] = tmp
    print xs

def bubble_sort(xs):
    for i in range(len(xs)):
        print xs
        for j in range(i+1, len(xs)):
            if xs[i] > xs[j]:
                tmp   = xs[i]
                xs[i] = xs[j]
                xs[j] = tmp
    print xs
