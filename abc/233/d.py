from collections import defaultdict


def main():
    N, K = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]

    As = [0]
 

    for i in range(N):
        As.append(As[i] + A[i])

    res = 0

    l = 0
    r = 1

    for l in range(0, N-1):
        for r in range(l+1, N):
            t = As[r] - As[l]

            if t == K:
                res += 1

    print(res)

if __name__ == '__main__':
    main()
