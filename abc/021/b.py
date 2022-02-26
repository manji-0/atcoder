def main():
    N = int(input())
    a, b = [ int(i) for i in input().split() ]
    K = int(input())
    P = [ int(i) for i in input().split() ]

    P.append(b)

    visited = set()

    for p in P:
        if p in visited:
            print("NO")
            return
        if p == a:
            print("NO")
            return
        visited.add(p)
    
    print("YES")

main()
#print(main())
