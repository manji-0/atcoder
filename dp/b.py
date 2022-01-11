def main():
    N, K = [ int(i) for i in input().split() ]
    H = [0] + [ int(i) for i in input().split() ]

    dp = [0] * (N+1)

    for i in range(2, N+1):
        print(dp[1:])
        for k in range(1, K+1):
            if i - k < 1:
                break

            cost = dp[i-k] + abs(H[i] - H[i-k])
            dp[i] = min(cost, dp[i]) if dp[i] > 0 else cost

    print(dp[N])

if __name__ == '__main__':
    main()
