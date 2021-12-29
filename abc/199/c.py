def main():
    N = int(input())
    S = input()
    Q = int(input())

    flip = 1

    S1 = list(S[:N])
    S2= list(S[N:])

    for _ in range(Q):
        t, a, b = [ int(i) for i in input().split() ]

        if t == 2:
            flip *= -1
            continue

        a -= 1
        b -= 1

        fa = fb = False

        if a >= N:
            a -= N
            fa = True
        if b >= N:
            b -= N
            fb = True
        
        if flip > 0:
            if fa:
                tmp = S2[a]

                S2[a] = S2[b]
                S2[b] = tmp
            else:
                tmp = S1[a]

                if fb:
                    S1[a] = S2[b]
                    S2[b] = tmp
                else:
                    S1[a] = S1[b]
                    S1[b] = tmp
        else:
            if fa:
                tmp = S1[a]

                S1[a] = S1[b]
                S1[b] = tmp
            else:
                tmp = S2[a]

                if fb:
                    S2[a] = S1[b]
                    S1[b] = tmp
                else:
                    S2[a] = S2[b]
                    S2[b] = tmp
                    
    if flip > 0:
        print(*(S1+S2), sep="")
    else:
        print(*(S2+S1), sep="")
        

if __name__ == '__main__':
    main()
