def main():
    S = input()
    N = len(S)

    dp = [ [0]*33 for _ in range(10**5+1) ]
    ans = [0] * (N)

    for i in range(N):
        if S[i] == 'R':
            dp[0][i] = i + 1
        else:
            dp[0][i] = i - 1

    for p in range(32):
        for i in range(N):
            dp[p+1][i] = dp[p][dp[p][i]]

    for i in range(N):
        ans[dp[32][i]] += 1

    print(*ans, sep=" ")

if __name__ == '__main__':
    main()
