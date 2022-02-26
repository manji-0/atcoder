from numpy import zeros

def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    ans = []

    dp = zeros((N, 2))
    dp[0][0] = 1
    dp[0][1] = A[0]

    for i in range(1,N):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] / A[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] * A[i])

    t = 0
    for i in range(N-1, -1, -1):
        if dp[i][t] == dp[i-1][t]:
            ans.append(0)
        else:
            ans.append(1)
            t = 0 if t else 1

    ans.reverse()

    print(*ans, sep=" ")        
    

if __name__ == '__main__':
    main()
