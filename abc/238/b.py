from mimetypes import init


def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    K = [0] * 360
    K[0] = 1
    c = 0

    for a in A:
        c = (c+a) % 360
        K[c] = 1

    ma = 0
    p = 0
    for i, k in enumerate(K):
        if k == 1:
            ma = max(i - p, ma)
            p = i

    ma = max(360-p, ma)

    print(ma)
    

main()
#print(main())
