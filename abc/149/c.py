def main():
    X = int(input())

    for p in makeprime(10**6):
        if p >= X:
            print(p)
            return

def makeprime(n):
    P = [ True for _ in range(n+1) ]

    P[0] = False
    P[1] = False

    for p, v in enumerate(P):
        if not v:
            continue

        yield p
        
        i = p
        while p * i <= n:
            P[p*i] = False
            i += 1

if __name__ == '__main__':
    main()
