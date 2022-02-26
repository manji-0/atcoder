def main():
    S = int(input())

    X1 = 0
    Y1 = 0
    Y2 = 0
    X3 = 0

    F = factor(S)

    X2 = F

    while ((X2 > 10**9) or (S//X2 > 10**9)):
        print(X2)
        x = factor(S//X2)

        if not x:
            X2 *= x
        
    Y3 = S // X2

    print(X1,Y1,X2,Y2,X3,Y3)

def factor(n):
    for i in range(2, int(-(-n**0.5//1))+1):
        if n%i==0:
            return i

if __name__ == '__main__':
    main()
