def main():
    T = int(input())

    Cases = [ [ int(i) for i in input().split() ] for _ in range(T) ]

    for n1,n2,n3 in Cases:
        print(make10(n1,n2,n3))

def make10(n1,n2,n3):
    ans = 0

    while n2 > 0 and n3 > 0:
        if n3 > 

if __name__ == '__main__':
    main()
