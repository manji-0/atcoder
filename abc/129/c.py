def main():
    N, M = [ int(i) for i in input().split() ]

    A = { int(input()) for _ in range(M) }
    BASE = 1000000007

    dp = [0] * 10**6

    dp[0] = 1

    for i in range(N):
        for d in range(1, 3):
            if (i+d) not in A:
                dp[i + d] += dp[i]
    
    print(dp[N] % BASE)

if __name__ == '__main__':
    main()
