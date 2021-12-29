def main():
    X, Y = [ int(i) for i in input().split() ]

    m = Y-X
    ten = 0

    while 1:
        if m <= 0:
            print(ten)
            return

        m -= 10
        ten += 1

if __name__ == '__main__':
    main()
