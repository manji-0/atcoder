from collections import deque

def main():
    N, M = [ int(i) for i in input().split() ]
    H = [ int(i) for i in input().split() ]
    M = [ [ int(i) for i in input().split() ] for _ in range(M) ]

    start = H[0]
    mi = 10**9
    mi_p = 10000

    uf = UnionFind(N)

    for f, t in M:
        uf.unite(f,t)

        if uf.is_same_root(f):
            mi = min(mi, H[f], H[t])
            if mi == H[f]:
                mi_p = f
            elif mi == H[t]:
                mi_p = t

    
    Q = deque()

    Q.append((1, 0))

    while Q:
        q = Q.popleft()

        
    
                

        

    

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [0] + [-1]*n
        self.rnk = [0]*(n+1)

    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)

        if(x == y):
            return

        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def is_same_root(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def union_size(self, x):
        return -self.root[self.find_root(x)]

    def __len__(self):
        return len([ i for i in self.root if i < 0 ])




main()
#print(main())
