def main():
    N, K = [ int(i) for i in input().split() ]
    R = [ int(i) for i in input().split() ]

    R.sort()

    R = R[N-K:]

    rate = 0
    for r in R:
        rate = (rate + r) / 2

    print(rate)

if __name__ == '__main__':
    main()
