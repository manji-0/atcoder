def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    s = A[0]

    for a in A:
        if s > a:
            break
        else:
            s = a

    ans = [ i for i in A if i != s ]

    print(*ans, sep=" ")

main()
#print(main())
