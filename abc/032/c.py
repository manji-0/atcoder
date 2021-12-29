def main():
    N, K = [ int(i) for i in input().split() ]
    S = [1] + [ int(input()) for _ in range(N) ]

    for i in range(N):
        if S[i] == 0:
            print(len(S))
            return

    r = 1
    l = 0
    pdt = S[r]
    ans = 0

    while r < N:
        if pdt <= K:
            ans = max(ans, r-l)
            r += 1
            if S[r] > K:
                l = r
                r += 1
                pdt = S[r]
            else:
                pdt *= S[r]
        else: 
            l += 1
            pdt = pdt // S[l]

    print(ans)

            

if __name__ == '__main__':
    main()
