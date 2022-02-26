def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    mi = min(A)
    f = True

    while f:
        A = [ i % mi if i % mi != 0 else mi for i in A ]

        m = min(A)

        if mi == m:
            f = False
        else:
            mi = m

    print(mi)

if __name__ == '__main__':
    main()
