from numpy import Inf
from collections import defaultdict

def main():
    a, N = [ int(i) for i in input().split() ]

    cnt = Inf

    stack = [(1,0)]
    seen = defaultdict(lambda: Inf)
    seen[1] = 0

    while stack:
        T = stack.pop()

        if T[0] == N:
            cnt = min(cnt, T[1])
            continue

        if T[1] > cnt:
            continue

        if len(str(T[0] * a)) <= len(str(N)):
            if T[1] + 1 < seen[T[0]*a]:
                stack.append((T[0] * a, T[1]+1))
                seen[T[0]*a] = T[1]+1

        next = str(T[0])

        if len(next) >= 2 and next[-1] != "0":
            rotate = int(next[-1] + next[0:len(next)-1])

            if seen[rotate] > T[1]+1 :
                seen[rotate] = T[1]+1
                stack.append((rotate, T[1]+1))

    if cnt == Inf:
        print(-1)
        return

    print(cnt)
            
if __name__ == '__main__':
    main()
