
def main():
    N, Q = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]
    Q = [ [ int(i) for i in input().split() ] for _ in range(Q) ]

    S = set(A)
    memo = dict()

    for s in S:
        memo[s] = [(-1,0),]
        
    for i, a in enumerate(A):
        memo[a].append((i, memo[a][-1][1]+1))

    for x, k in Q:
        if x not in memo:
            print(-1)
            continue

        t = memo[x]

        if t[-1][1] < k:
            print(-1)
            continue

        ok = len(t)+1
        ng = 0

        while ok-ng > 1:
            mid = (ok+ng) // 2
            
            if t[mid][1] >= k:
                ok = mid
            else:
                ng = mid

        print(t[ok][0]+1)

if __name__ == '__main__':
    main()
