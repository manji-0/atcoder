def main():
    N, M = [ int(i) for i in input().split() ]
    S = [ i for i in input().split() ]
    T = [ i for i in input().split() ]

    Td = set()

    for t in T:
        Td.add(t)

    for s in S:
        if s in Td:
            print("Yes")
        else:
            print("No")
    
main()
#print(main())
