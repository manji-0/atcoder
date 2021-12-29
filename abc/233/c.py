def main():
    N, X = [ int(i) for i in input().split() ]

    L = [ [ int(i) for i in input().split() ] for _ in range(N) ]
    Ln = []

    for i in range(N):
        Ln.append(L[i][0])
        L[i] = L[i][1:]
        L[i].sort()

    res = 0

    idx = [0] * N

    while True:
        prd = 1

        for n in range(N):
            prd *= L[n][idx[n]]

        if prd == X:
            res += 1

        for n in range(N):
            if idx[n] < Ln[n] - 1:
                idx[n] += 1
                for nn in range(n):
                    idx[nn] = 0
                break

        
        if idx == [ i - 1 for i in Ln ]:
            prd = 1

            for n in range(N):
                prd *= L[n][idx[n]]

            if prd == X:
                res += 1

            break
    
    print(res)
    

if __name__ == '__main__':
    main()
