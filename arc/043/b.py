from numpy import zeros

def main():
    N = int(input())
    D = [ int(input()) for _ in range(N) ]
    D.sort()

    dp = zeros((N, 4))

    


if __name__ == '__main__':
    main()
