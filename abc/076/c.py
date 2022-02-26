from math import factorial
def main():
    N, M = [ int(i) for i in input().split() ]
    MOD = 10**9+7

    n = factorial(N) % MOD
    m = factorial(M) % MOD
    
    if N == M:
        print(2 * n*m % MOD)
    elif abs(N-M) == 1:
        print(n*m % MOD)
    else:
        print(0)

main()
#print(main())
