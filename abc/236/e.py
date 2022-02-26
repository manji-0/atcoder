N = int(input())
A = [ int(i) for i in input().split() ]

def main():
    ma = 10**12+1
    mi = N*10**3

    while (ma-mi) > 1:
        mid = (ma+mi)//2

        if avgOK(mid):
            ma = mid
        else:
            mi = mid

    ans1 = ma

    ma = 10**9+1
    mi = N

    while (ma-mi) > 1:
        mid = (ma+mi) // 2

        if midOK(mid):
            ma = mid
        else:
            mi = mid

    ans2 = ma
    
    print(ans1//10**3, ans2)

def avgOK(k):
    dp1 = [0]
    dp2 = [0]

    for a in A:
        a = a*10**3-k
        print(a)

        dp1.append(max(dp1[-1], dp2[-1]))
        dp2.append(max(dp1[-2]+a, dp2[-1]+a))

    print(max(dp1[-1], dp2[-1]))

    return max(dp1[-1], dp2[-1])

def midOK(k):
    dp1 = [0]
    dp2 = [0]

    for a in A:
        a = 1 if a >= k else -1

        dp1.append(max(dp1[-1], dp2[-1]))
        dp2.append(max(dp1[-2]+a, dp2[-1]+a))

    return max(dp1[-1], dp2[-1])    

    

main()
#print(main())
