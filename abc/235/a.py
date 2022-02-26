def main():
    A,B,C = [ int(i) for i in input() ]

    a = 100*A+10*B+C
    b = 100*B+10*C+A
    c = 100*C+10*A+B

    print(a+b+c)

if __name__ == '__main__':
    main()
