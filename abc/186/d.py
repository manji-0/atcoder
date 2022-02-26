def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    A.sort()

    ans = 0

    for i in range(1, N):
        ans += A[i] - 

    print(ans)

if __name__ == '__main__':
    main()
