def bubble_sort(a):
    n = len(a)
    # p reprsent passes, total n-1 passes
    for p in range(n - 1):
        # in first pass when p = 0, j = 0 to n - 2 (both inclusive)
        # in second pass when p = 1, j = 0 to n - 3
        # ...
        # in last pass when p = n - 2, j = 0
        for j in range(n - p - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def main():
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    bubble_sort(a)
    print(a)

if __name__ == "__main__":
    main()
