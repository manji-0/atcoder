def main():
    N = int(input())

    T = [None]

    for _ in range(1, N+1):
        a = [ int(i) for i in input().split() ]

        Tn = a[0]
        A = a[2:]

        T.append((Tn, set(A)))

    toCheck = [N]
    toLearn = set([N])

    while toCheck:
        check = T[toCheck.pop()]

        tmp = check[1] - toLearn

        if len(tmp):
            toCheck += list(tmp)
            toLearn = toLearn.union(tmp)

    ans = sum([ T[i][0] for i in toLearn ])

    print(ans)

if __name__ == '__main__':
    main()
