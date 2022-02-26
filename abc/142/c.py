def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    at = dict()

    for i in range(N):
        at[A[i]] = i+1

    ans = []

    for i in range(1, N+1):
        ans.append(at[i])

    print(*ans, sep=" ")



if __name__ == '__main__':
    main()
