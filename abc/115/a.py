def main():
    N,M = [ int(i) for i in input().split() ]
    S = [ int(input()) for _ in range(N) ]

    ans = 0

    for i in range(N-1):
        for j in range(i+1, N):
            a = 0
            s = str(S[i] + S[j])

            for 

            if a % 2 == 1:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
