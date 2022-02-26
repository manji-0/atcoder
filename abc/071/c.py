from collections import defaultdict

def main():
    N = int(input())
    S = [ input() for _ in range(N) ]

    l = set()
    d = []

    for _ in range(N):
        d.append(defaultdict(int))

    for i, s in enumerate(S):
        for c in s:
            l.add(c)
            d[i][c] += 1

    ans = []

    l = sorted(l)

    for c in l:
        mi = 50
        for i in range(N):
            mi = min(mi, d[i][c])
        
        for _ in range(mi):
            ans.append(c)

    print(*ans, sep="")

main()
#print(main())
