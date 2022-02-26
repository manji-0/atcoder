def main():
    A, B, X = [ int(i) for i in input().split() ]

    ma = 10**9 + 1
    mi = 0

    while (ma-mi) > 1:
        mid = (ma+mi)//2

        if (A * mid + B * len(format(mid, 'd'))) > X:
            ma = mid
        else:
            mi = mid

    print(mi)

if __name__ == '__main__':
    main()
