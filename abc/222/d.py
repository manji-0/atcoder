def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]
    B = [ int(i) for i in input().split() ]
    MOD = 998244353
    L = 3000

    dp = [1] * (L+1)

    for i in range(N):
        nx = [0] * (L+1)

        for j in range(A[i], B[i]+1):
            nx[j] = dp[j]

        dp = nx

        for i in range(L):
            dp[i+1] += dp[i]
            dp[i+1] %= MOD

    print(dp[L])

main()
#print(main())
