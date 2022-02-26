def main():
    N, Q = [ int(i) for i in input().split() ]

    tails = [0] * (N+1)
    heads = [0] * (N+1)

    Q = [ [ int(i) for i in input().split() ] for _ in range(Q) ]

    for q in Q:
        if q[0] == 1:
            tails[q[1]] = q[2]
            heads[q[2]] = q[1]
        elif q[0] == 2:
            tails[q[1]] = 0
            heads[q[2]] = 0
        elif q[0] == 3:
            x = q[1]

            while heads[x] != 0:
                x = heads[x]

            l = []
            c = 0
            while True:
                l.append(x)
                c += 1
                x = tails[x]
                if x == 0:
                    break

            print(c, *l, sep=" ")

if __name__ == '__main__':
    main()
