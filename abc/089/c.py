from collections import defaultdict
from itertools import product

def main():
    N = int(input())
    S = [ input() for _ in range(N) ]
    H = "MARCH"

    march = defaultdict(int)

    for s in S:
        if s[0] in H:
            march[s[0]] += 1

    ans = 0

    for i in product([1, 0], repeat=5):
        if sum(i) != 3:
            continue

        tmp = 1

        for j, v in enumerate(i):
            if v:
                tmp *= march[H[j]]

        ans += tmp

    print(ans)

if __name__ == '__main__':
    main()
