def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]
    MOD = 10**9+7

    S = sum(A)

    ans = 0

    for a in A[:N-1]:
        S -= a
        ans = (ans+(a*S)) % MOD
        
    print(ans)
    

main()
#print(main())
