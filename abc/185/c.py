from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)

def main():
    L = int(input())

    if L == 12:
        print(1)
        return

    print(sp(L-12, 12))

@lru_cache(maxsize=None)
def sp(l, n):
    if l == 0:
        return 0
    if n == 1:
        return 1

    ans = 1
    for i in range(l):
        ans += sp(l-i, n-1)

    return ans

main()
#print(main())
