def main():
    S = list(input())
    N = int(input())

    for _ in range(N):
        l, r = [ int(i)-1 for i in input().split() ]

        rev(S, l, r)

    print(*S, sep="")

def rev(S, l, r):
    while r > l:
        tmp = S[l]
        S[l] = S[r]
        S[r] = tmp

        l += 1
        r -= 1

if __name__ == '__main__':
    main()
