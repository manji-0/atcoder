
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)

    def sum(self, i):
        s = 0

        while i > 0:
            s += self.data[i]
            i -= i & -i

        return s

    def add(self, i, x):
        # assert i > 0
        self.el[i] += x

        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]

        return self.sum(j) - self.sum(i)

    def lower_bound(self, w):
        if w <= 0:
            return 0

        x = 0
        r = 1

        while (r < self.n):
            r << 1

        l = r

        while l > 0:
            if x + l < self.n and self.data[x+l] < w:
                w -= self.data[x+l]
                x += l
                l >> 1
        
        return x + l

def main():
    N, K = [ int(i) for i in input().split() ]
    P = [ int(i) for i in input().split() ]

    B = BIT(N)

    for k in P[:K]:
        B.add(N-k+1, 1)

    for k in P[K:]:
        ma = N+2
        mi = 0

        while (ma-mi) > 1:
            mid = (ma+mi)//2

            if B.sum(mid) >= K:
                ma = mid
            else:
                mi = mid

        print(N-ma+1)

        B.add(N-k+1, 1)

    ma = N+2
    mi = 0

    while (ma-mi) > 1:
        mid = (ma+mi)//2

        if B.sum(mid) >= K:
            ma = mid
        else:
            mi = mid

    print(N-ma+1)

if __name__ == '__main__':
    main()
