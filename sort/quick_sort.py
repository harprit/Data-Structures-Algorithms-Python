def quick_sort(a):
    quick_sort_rec(a, 0, len(a) - 1)


def quick_sort_rec(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort_rec(a, p, q - 1)
        quick_sort_rec(a, q + 1, r)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i

a = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(a)
print(a)
