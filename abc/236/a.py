def main():
    S = list(input())
    a, b = [ int(i) for i in input().split() ]
    tmp = S[a-1]

    S[a-1] = S[b-1]
    S[b-1] = tmp

    print(*S, sep="")


main()
#print(main())
