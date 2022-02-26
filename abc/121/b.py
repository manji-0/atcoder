def main():
    N, M, C = [ int(i) for i in input().split() ]

    B = [ int(i) for i in input().split() ]
    A = [ [ int(i) for i in input().split() ] for _ in range(N) ]

    ans = 0

    for n in range(N):
        s = C

        for m in range(M):
            s += A[n][m]*B[m]

        if s > 0:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
