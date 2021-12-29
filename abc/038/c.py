def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    stack = []

    for i in range(N):
        stack.append([i])

    ans = N

    while stack:
        l = stack.pop()
        
        if l[-1] == N-1:
            continue

        if A[l[-1]] <= A[l[-1]+1]:
            ans += 1
            l.append(l[-1]+1)
            stack.append(l)

    print(ans)
        

if __name__ == '__main__':
    main()
