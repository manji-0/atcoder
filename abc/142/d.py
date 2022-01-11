from collections import defaultdict
from math import gcd

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
    A, B = [ int(i) for i in input().split() ]

    GCD = gcd(A, B)

    if GCD == 1:
        print(1)
        return

    print(len(factorization(GCD))+1)

if __name__ == '__main__':
    main()
