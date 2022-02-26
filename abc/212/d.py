import heapq

def main():
    Q = int(input())
    Q = [ tuple(input().split()) for _ in range(Q) ]

    B = []
    Add = 0
    ans = []

    for q in Q:
        if q[0] == "1":
            heapq.heappush(B, int(q[1])-Add)
        elif q[0] == "2":
            Add += int(q[1])
        else:
            a = heapq.heappop(B)
            ans.append(a+Add)

    for a in ans:
        print(a)

main()
#print(main())
