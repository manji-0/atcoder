def main():
    N, M, Q = [ int(i) for i in input().split() ]

    Paths = [ [ int(i) for i in input().split() ] for _ in range(M) ]
    Queries = [ [ int(i) for i in input().split() ] for _ in range(Q) ]

    Paths.sort(key=lambda x: x[2])

    for q in Queries:
        T = UnionFind(N)
        p = set()

        for P in Paths:
            if P[2] >= q[2]:
                if not T.is_same_root(q[0], q[1]):
                    p.add(tuple(q))
                    break
            
            if not T.is_same_root(P[0], P[1]):
                T.unite(P[0], P[1])
                p.add(tuple(P))

        if tuple(q) not in p:
            print("No")
        
        
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



if __name__ == '__main__':
    main()
