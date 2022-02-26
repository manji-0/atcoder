def main():
    N, X = [ int(i) for i in input().split() ]
    J = [ [ int(i) for i in input().split() ] for _ in range(N) ]

    A = []
    As = 0
    B = []
    Bs = 0

    for a,b in J:
        A.append(a)
        As += a
        B.append(b)
        Bs += b

    if As > X or Bs < X:
        print("No")
        return

    S = set([A[0], B[0]])

    for j in range(1, N):
        C = list(S)
        T = set()

        for c in C:
            T.add(c+A[j])
            T.add(c+B[j])

        S = T

    if X in S:
        print("Yes")
    else:
        print("No")

    

    

main()
#print(main())
