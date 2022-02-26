def main():
    N = int(input())
    V = [ int(i) for i in input().split() ]

    V.sort()

    ans = V[0]

    for v in V[1:]:
        ans = (ans + v) / 2

    print(ans)

if __name__ == '__main__':
    main()
