def main():
    N, M = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]
    B = [ int(i) for i in input().split() ]

    A.sort()
    B.sort()

    mi = 10**9+1

    for a in A:
        if B[-1] < a:
            mi = min(mi, a-B[-1])
            continue
        elif B[0] >= a:
            mi = min(mi, B[0]-a)
            continue

        ok = M
        ng = 0

        while ok-ng > 1:
            mid = (ok+ng) // 2
            
            if B[mid] >= a:
                ok = mid
            else:
                ng = mid

        mi = min(mi,B[ok]-a)
        mi = min(mi, a-B[ng])

    print(mi)

main()
#print(main())
