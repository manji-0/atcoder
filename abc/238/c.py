def main():
    N = input()

    ans = 0
    M = 998244353
    L = len(N)
    N = int(N)

    if L == 1:
        print(N*(N+1)//2)
        return

    for i in range(1, L):
        x = (9*10**(i-1))
        ans += x*(x+1)//2
        ans %= M

    N = N - 10**(L-1)+1
    ans += N*(N+1)//2
    ans %= M

    print(ans)
    
        
main()
#print(main())
