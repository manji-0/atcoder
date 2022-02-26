
def main():
    n = int(input())
    R = [ (i,int(v)) for i, v in enumerate(input().split()) ]
    C = [ (i,int(v)) for i, v in enumerate(input().split()) ]
    q = int(input())

    k = lambda x: x[1]
    R.sort(key=k)
    C.sort(key=k)

    N = []
 
    for i in range(1, n+1):
        f = [ a*i for a in range(n) ]
        N.append(f)

    r = n-1
    l = 0

    while r >= l:
        r1 = R[r][0]
        r2 = C[r][0]
        l1 = R[l][0]
        l2 = C[l][0]

        for i in range(n):
            if N[r1][i] != ".":
                N[r1][i] = "#"
            if N[i][r2] != ".":
                N[i][r2] = "#"
            if N[l1][i] != "#":
                N[l1][i] = "."
            if N[i][l2] != "#":
                N[i][l2] = "."   
        
        r -= 1
        l += 1     

    rc = [ [ int(i) - 1 for i in input().split() ] for _ in range(q) ]

    print(*[ N[i[0]][i[1]] for i in rc ], sep="")

if __name__ == '__main__':
    main()
