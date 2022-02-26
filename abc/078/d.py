def main():
    N, Z, W = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]
    
    i = 0

    while i < N:
        ma = max(A[i:])
        macnt = A[i:].count(ma)

        j = 0
        while j != macnt:
            c = A[i]
            i += 1
            if c == ma:
                j += 1
        Z = ma
        
        if i >= N:
            break

        mi = min(A[i:])
        micnt = A[i:].count(mi)

        j = 0
        while j != micnt:
            c = A[i]
            i += 1
            if c == mi:
                j += 1
        W = mi

    print(abs(Z-W))

if __name__ == '__main__':
    main()
