def main():
    N, M = [ int(i) for i in input().split() ]

    D = [ [ int(i) for i in input().split() ] for _ in range(N) ]

    D.sort(key=lambda x: x[0])

    ans = 0

    for d in D:
        if d[1] <= M:
            ans += d[0]*d[1]
            M -= d[1]
        else:
            ans += d[0] * M
            break

    print(ans)

if __name__ == '__main__':
    main()
