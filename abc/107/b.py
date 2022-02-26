def main():
    H, W = [ int(i) for i in input().split() ]

    A = [ list(input()) for _ in range(H) ]

    for h in range(H):
        flag = True
        for w in range(W):
            if A[h][w] != '.':
                flag = False

        if flag:
            for w in range(W):
                A[h][w] = ''

    for w in range(W):
        flag = True
        for h in range(H):
            if A[h][w] not in ['', '.']:
                flag = False

        if flag:
            for h in range(H):
                A[h][w] = ''

    for h in range(H):
        if set(A[h]) == {''}:
            continue
        
        print(*A[h], sep="")
            
if __name__ == '__main__':
    main()
