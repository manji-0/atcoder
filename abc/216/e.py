import heapq

def main():
    N, K = [ int(i) for i in input().split() ]
    A = [ int(i) * (-1) for i in input().split() ]

    heapq.heapify(A)

    ans = 0

    for _ in range(K):
        a = heapq.heappop(A)
        ans += -a

        if a+1 != 0:
            heapq.heappush(A, a+1)

    print(ans)

if __name__ == '__main__':
    main()
