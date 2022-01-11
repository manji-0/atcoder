def main():
    N = int(input())
    H = [0] + [ int(i) for i in input().split() ]

    dp = [0] * (N+1)

    for i in range(2,N+1):
        cos1 = dp[i-1] + abs(H[i]-H[i-1])
        dp[i] = min(cos1, dp[i]) if dp[i] > 0 else cos1

        if i > 2:
            cos2 = dp[i-2] + abs(H[i]-H[i-2])
            dp[i] = min(cos2, dp[i]) if dp[i] > 0 else cos2    

    print(dp[N])

if __name__ == '__main__':
    main()
