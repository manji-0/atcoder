def main():
    A,B,C,D = [ int(i) for i in input().split() ]

    S = set(makeprime(200))

    for t in range(A,B+1):
        if sum([ int(t+a in S) for a in range(C,D+1)]) == 0:
            print("Takahashi")
            return

    print("Aoki")

def makeprime(n):
    P = [ True for _ in range(n+1) ]

    P[0] = False
    P[1] = False

    for p, v in enumerate(P):
        if not v:
            continue

        yield p
        
        i = p
        while p * i <= n:
            P[p*i] = False
            i += 1

main()
#print(main())
