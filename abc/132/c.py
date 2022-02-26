def main():
    N = int(input())
    D = [ int(i) for i in input().split() ]

    D.sort()

    i = 0
    p = 0
    cnt = 0

    for k in range(0,10**5+1):
        while i < N and D[i] < k:
            p += 1
            i += 1

        if p == N//2:
            cnt += 1
        elif p > N//2:
            break

    print(cnt)

if __name__ == '__main__':
    main()
