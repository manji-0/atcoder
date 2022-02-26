def main():
    N, K = [ int(i) for i in input().split() ]
    mi = min(N%K, K-N%K)

    print(mi)

if __name__ == '__main__':
    main()
