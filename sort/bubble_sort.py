def bubblesort(a):
    n = len(a)
    # i reprsent passes, total n-1 passes
    for i in range(n - 1):
        # in first pass when i = 0, j = 0 to n - 2 (both inclusive)
        # in second pass when i = 1, j = 0 to n - 3
        # ...
        # in last pass when i = n - 2, j = 0
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def main():
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    bubblesort(a)
    print(a)

if __name__ == "__main__":
    main()
