def main():
    N = int(input())
    A = [ [ int(i) for i in input().split() ] for _ in range(N-1) ]

    A.sort(key=lambda x: min(x))

    T = { i: [ -1, set() ] for i in range(1, N+1) }
    T[1][0] = 0

    Ts = [ set([i]) for i in range(N+1) ]

    for u, v in A:
        if T[u][0] == T[v][0] == -1:
            A.append([u,v])
        elif T[u][0] != -1:
            T[u][1].add(v)
            T[v][0] = u
        else:
            T[v][1].add(u)
            T[u][0] = v

    Tk = sorted(T.keys(), key=lambda x: len(T[x][1]))

    for t in Tk:
        T[T[t][0]][1].unite(T[t][1])

main()
#print(main())
