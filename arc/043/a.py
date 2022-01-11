def main():
    N, A, B = [ int(i) for i in input().split() ]

    ma = 0
    mi = 10 ** 10 + 1
    avg = 0

    for _ in range(N):
        p = int(input())

        ma = max(ma, p)
        mi = min(mi, p)
        avg += p

    if ma - mi == 0:
        print(-1)
        return

    P = B / (ma - mi)

    avg = P * avg / N

    Q = A - avg

    print(P, Q)
    

if __name__ == '__main__':
    main()
