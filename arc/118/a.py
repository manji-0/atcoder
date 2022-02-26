import numpy as np

def main():
    t, N = [ int(i) for i in input().split() ]

    P = 100 + t

    A = np.ones(P, np.bool_)

    for x in range(100):
        A[P*x // 100] = 0

    B = np.where(A)[0]
    q, r = divmod(N-1, t)
    ans = P * q + B[r]
    print(ans)

if __name__ == '__main__':
    main()
