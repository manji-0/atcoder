def main():
    K, N = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]

    ma = min(A[N-1]-A[0], K-A[N-1]+A[0])

    for i in range(0, N-1):
        ma = max(ma, A[i+1]-A[i])

    print(K-ma)

if __name__ == '__main__':
    main()
