def main():
    N = int(input())

    ma = 0

    P = [ [ int(i) for i in input().split() ] for _ in range(N) ]

    for i, p1 in enumerate(P):
        for p2 in P[i+1:]:
            ma = max(ma, l(p1,p2))

    print(ma)

def l(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)

if __name__ == '__main__':
    main()
