def main():
    N, M = [ int(i) for i in input().split() ]

    W = [ int(input()) for _ in range(M) ]
    W.reverse()

    Hist = [False] * (N+1)

    for w in W:
        if not Hist[w]:
            print(w)
            Hist[w] = True
    
    for i, v in enumerate(Hist[1:]):
        if v is False:
            print(i+1)

if __name__ == '__main__':
    main()
