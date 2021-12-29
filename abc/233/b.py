def main():
    L, R = [ int(i) for i in input().split() ]
    S = list(input())

    while R > L:
        tmp = S[R-1]
        S[R-1] = S[L-1]
        S[L-1] = tmp
        L += 1
        R -= 1

    print(*S, sep="")

if __name__ == '__main__':
    main()
