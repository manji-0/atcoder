def main():
    N, K = [ int(i) for i in input().split() ]

    print(K*(K-1)**(N-1))

if __name__ == '__main__':
    main()
