from collections import defaultdict


def main():
    N, K = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]

    As = [0]
 

    for i in range(N):
        As.append(As[i] + A[i])

    print(As)

    res = 0
    mp = defaultdict(int)

    for r in range(1, N+1):
        mp[As[r-1]] += 1
        res += mp[As[r]-K]
        print(mp)

    print(res)

if __name__ == '__main__':
    main()
