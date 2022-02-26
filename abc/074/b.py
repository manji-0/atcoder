def main():
    N = int(input())
    K = int(input())
    X = [0] + [ int(i) for i in input().split() ]

    ans = 0

    for i in range(1, N+1):
        ans += min(X[i], abs(X[i]-K)) * 2
    
    print(ans)

if __name__ == '__main__':
    main()
