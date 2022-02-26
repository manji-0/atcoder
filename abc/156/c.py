def main():
    N = int(input())
    X = [ int(i) for i in input().split() ]

    mi = (100**2)*N

    for i in range(1,101):
        su = 0

        for j in X:
            su += (i-j)**2

        mi = min(mi, su)
    
    print(mi)

if __name__ == '__main__':
    main()
