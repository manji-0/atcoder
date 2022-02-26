from math import gcd

def main():
    N, M = [ int(i) for i in input().split() ]
    S = input()
    T = input()

    if S[0] != T[0]:
        print(-1)
        return

    l = N*M // gcd(N,M)
    si = 0
    ti = 0
    s = ""
    t = ""

    text = ""
    for c in range(1,l+1):
        if (c-1) * (l//N) + 1 == (c-1) * (l//M) + 1:
            

    if s == S and t == T:
        print(l)
        return

    print(-1)
        

if __name__ == '__main__':
    main()
