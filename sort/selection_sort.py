def selection_sort(a):
    n = len(a)
    for p in range(n - 1):
        min_value_index = find_min_value_index(a, p, n)
        if min_value_index != p:
            a[p], a[min_value_index] = a[min_value_index], a[p]


def find_min_value_index(a, beg, end):
    min_value_index = beg
    for i in range(beg, end):
        if a[i] < a[min_value_index]:
            min_value_index = i
    return min_value_index


def main():
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    selection_sort(a)
    print(a)

if __name__ == "__main__":
    main()
