import heapq

def main():
    N, M = [ int(i) for i in input().split() ]
    A = [ int(i) * (-1) for i in input().split() ]

    heapq.heapify(A)

    for _ in range(M):
        a = heapq.heappop(A)
        a = (-1) * a // 2

        heapq.heappush(A, -a)

    print(-sum(A))

if __name__ == '__main__':
    main()
