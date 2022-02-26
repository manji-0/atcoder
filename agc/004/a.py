def main():
    A, B, C = [ int(i) for i in input().split() ]

    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        print(0)
        return

    print(min(A*B, B*C, C*A))

if __name__ == '__main__':
    main()
