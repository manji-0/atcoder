def main():
    N, M, X = [ int(i) for i in input().split() ]
    A = set([ int(i) for i in input().split() ])

    forN = 0
    for0 = 0

    for i in range(X,N):
        if i in A:
            forN += 1

    for i in range(0,X):
        if i in A:
            for0 += 1

    ans = min(forN,for0)

    print(ans)
    

if __name__ == '__main__':
    main()
