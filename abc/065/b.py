def main():
    N = int(input())
    A = [0] + [ int(input()) for _ in range(N) ]

    seen=set([1])
    nxt = A[1]
    cnt = 1

    if nxt == 2:
        print(1)
        return

    while True:
        seen.add(nxt)
        nxt = A[nxt]
        cnt += 1

        if nxt == 2:
            print(cnt)
            return
        elif nxt in seen:
            break

    print(-1)
    

if __name__ == '__main__':
    main()
