from collections import defaultdict


def main():
    N, K = [ int(i) for i in input().split() ]
    C = [ int(i) for i in input().split() ]

    D = defaultdict(int)

    for i in range(K):
        D[C[i]] += 1

    S = set([ c for c in D if D[c] > 0 ])

    ans = len(S)

    for i in range(K, N):
        D[C[i-K]] -= 1
        if D[C[i-K]] == 0:
            S.discard(C[i-K])
        
        if D[C[i]] == 0:
            S.add(C[i])
        
        D[C[i]] += 1
        
        ans = max(len(S), ans)

    print(ans)

main()
#print(main())
