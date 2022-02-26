from math import gcd


def main():
    N, M = [ int(i) for i in input().split() ]
    A = [ int(i) for i in input().split() ]
    ans = [1]
    lcm = 1

    for a in A:
        lcm = lcm*a // gcd(lcm, a)

    for i in range(2, M+1):
        if gcd(lcm, i) == 1:
            ans.append(i)

    print(len(ans))
    for a in ans:
        print(a)

main()
#print(main())
