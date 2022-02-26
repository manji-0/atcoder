def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    current = 0

    As = [A[0]]
    Ap = [A[0]]
    pre_p = 0
    pre_n = 0
    ma = 0

    for i in range(1, N):
        if A[i] > 0:
            pre_p += A[i]
            As.append(max(pre_p+pre_n, ma))
            pre_n = 0
        else:
            pre_n += A[i]
            As.append(max(pre_p+pre_n, ma))
            pre_p = 0
        Ap.append(Ap[-1]+Ap[-1]+A[i])



    for i in range(1, N+1):
        for j in range(0, i):
            current += A[j]
            print(current)
            ma = max(ma, current)

    print(As)
    print(Ap)
        

main()
#print(main())
