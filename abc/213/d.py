from numpy import zeros

def main():
    N = int(input())
    M = [ [ int(i) for i in input().split() ] for _ in range(N-1) ]

    P = zeros((N+1,N+1))
    Nxt = [list()]
    visited = set()
    current = 1
    pre = dict()

    for _ in range(N):
        Nxt.append([])

    for a, b in M:
        Nxt[a].append(b)
        Nxt[b].append(a)

    for nx in Nxt:
        nx.sort(reverse=True)

    ans = []

    while 1:
        ans.append(current)
        visited.add(current)

        while 1:
            if not Nxt[current]:
                if current == 1:
                    print(*ans, sep=" ")
                    return
                else:
                    current = pre[current]
                    break

            n = Nxt[current].pop()
            if n not in visited:
                pre[n] = current
                current = n
                break
        

main()
#print(main())
