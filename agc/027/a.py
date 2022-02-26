def main():
    N, X = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]

    if sum(A) < X:
        print(N-1)
        return

    A.sort()
    cnt = 0

    for a in A:
        X -= a
        if X >= 0:
            cnt += 1
        else:
            break

    if X > 0:
        cnt -= 1

    print(cnt)
    

if __name__ == '__main__':
    main()
