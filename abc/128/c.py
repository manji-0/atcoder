from itertools import product


def main():
    N, M = [ int(i) for i in input().split() ]

    S = []

    P = [ [1, 0] for _ in range(N) ]

    for _ in range(M):
        S.append([ int(i) - 1 for i in input().split() ][1:])

    On = [ int(i) for i in input().split() ]

    ans = 0

    for p in product(*P):
        count = 0

        for j, s in enumerate(S):
            res = sum([ p[i] for i in s ])

            if res % 2 == On[j]:
                count += 1

        if count == M:
            ans += 1

    print(ans)
    
if __name__ == '__main__':
    main()
