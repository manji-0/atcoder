def main():
    N = int(input())
    P = [ int(i) for i in input().split() ]
    Q = [ int(i) for i in input().split() ]

    Qi = [ 0 for _ in range(N+1) ]

    for i, v in enumerate(Q):
        Qi[v] = i

    ma = 0

    for i in range(N):
        # (p_idx, q_idx, len)
        stack = [(i, 0, 0)]
        
        while stack:
            p_idx, q_idx, l = stack.pop()
            p = P[p_idx]

            for q in range(p, N+1, p):
                if Qi[q] >= q_idx:
                    stack.append((p_idx+1, Qi[q], l+1))

main()

#import time
#s=time.time()
#main()
#e=time.time()
#print(e-s)
#print(main())
