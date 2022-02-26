def main():
    N,Q = [ int(i) for i in input().split() ]
    S = list(input())
    Q = [ [ int(i) for i in input().split() ] for _ in range(Q) ]

    Sn = [0, 0]

    for i in range(1, N):
        if S[i-1] == "A" and S[i] == "C":
            Sn.append(Sn[-1]+1)
        else:
            Sn.append(Sn[-1])

    for q in Q:
        l, r = q
        print(Sn[r]-Sn[l])

if __name__ == '__main__':
    main()
