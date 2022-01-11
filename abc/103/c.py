from math import gcd

def main():
    N = int(input())
    A = [ int(i) for i in input().split() ]

    B = 1

    for a in A:
        B = a*B // gcd(a,B)
    
    B -= 1

    print(sum([ B % i for i in A ]))

if __name__ == '__main__':
    main()
