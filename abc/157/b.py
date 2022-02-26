def main():
    A = [ int(i) for i in input().split() ] + [ int(i) for i in input().split() ] + [ int(i) for i in input().split() ]
    N = int(input())
    B = [ int(input()) for _ in range(N) ]

    for b in B:
        for i, a in enumerate(A):
            if a == b:
                A[i] = 0

    for i in range(0, 9, 3):
        if A[i] + A[i+1] + A[i+2] == 0:
            print('Yes')
            return

    for i in range(0,3):
        if A[i] + A[i+3] + A[i+6] == 0:
            print('Yes')
            return

    if A[0] + A[4] + A[8] == 0:
        print('Yes')
        return

    if A[2] + A[4] + A[6] == 0:
        print("Yes")
        return

    print("No")

           

if __name__ == '__main__':
    main()
