def main():
    N = int(input())

    dp = [ [0] * 3 for _ in range(N) ]

    dp[0] = [ int(i) for i in input().split() ]

    for i in range(1, N):
        a,b,c = [ int(i) for i in input().split() ]

        dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
        dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
        dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)

    print(max(dp[N-1]))

if __name__ == '__main__':
    main()
