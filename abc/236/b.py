from collections import defaultdict

def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    S = set([ i for i in range(1,N+1) ])
    D = defaultdict(int)

    for a in A:
        D[a] += 1
        if D[a] == 4:
            S.remove(a)

    print(S.pop())
    
main()
#print(main())
