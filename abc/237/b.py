import numpy as np

def main():
    H, W = [ int(i) for i in input().split() ]
    A = [ [ int(i) for i in input().split() ] for _ in range(H) ]

    A = np.array(A)

    A = A.T

    for a in A:
        print(*a, sep=" ")

main()
#print(main())
